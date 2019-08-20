package com.example.getappengine

import android.os.Build
import android.os.Bundle
import android.os.StrictMode
import android.text.Editable
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.fragment.app.Fragment
import kotlinx.android.synthetic.main.login_fragment.*
import kotlinx.android.synthetic.main.login_fragment.view.*
import okhttp3.*
import org.jetbrains.anko.doAsync
import org.jetbrains.anko.uiThread
import org.json.JSONArray
import org.json.JSONObject
import kotlin.reflect.typeOf

/**
 * Fragment representing the login screen for Shrine.
 */
class LoginFragment : Fragment() {

    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?, savedInstanceState: Bundle?): View? {

        if (Build.VERSION.SDK_INT >= 9) {
            val policy = StrictMode.ThreadPolicy.Builder().permitAll().build()
            StrictMode.setThreadPolicy(policy)
        }
        // Inflate the layout for this fragment
        val view = inflater.inflate(R.layout.login_fragment, container, false)

        view.next_button.setOnClickListener({
            if (!isPasswordValid(password_edit_text.text!!)) {
                password_text_input.error = getString(R.string.error_password)
            } else {
                // Clear the error.
                password_text_input.error = null
                // Navigate to the next Fragment.
                if (checkInfo()) {
                    val gotresponse = fetchInfo()
                    val jsonobject = JSONObject(gotresponse)

                    Global.setuserid(jsonobject.getString("pk"))
                    Global.setusername(jsonobject.getString("username"))
                    (activity as NavigationHost).navigateTo(FunctionsFragment(), false)
                }
                else{
                    next_button.error = "User Invalid"
                    password_text_input.error = "User Invalid"
                }
            }
        })

        // Clear the error once more than 8 characters are typed.
        view.password_edit_text.setOnKeyListener({ _, _, _ ->
            if (isPasswordValid(password_edit_text.text!!)) {
                // Clear the error.
                password_text_input.error = null
            }
            false
        })
        return view
    }

    // Gets a string from the apad19 which is formatted as
    //  an Array of JSON objects: [{...},{...},...{...}]
    private fun checkInfo(): Boolean {
        val url = "http://psevents.appspot.com/api/v1/rest-auth/login/"

        val username = username_edit_text.text.toString()
        val password = password_edit_text.text.toString()

        val json = """
            {
                "username":"${username}",
                "password":"${password}"
            }
            """.trimIndent()

        val body = RequestBody.create(MediaType.parse("application/json; charset=utf-8"), json)

        val client = OkHttpClient()
        val request = Request.Builder()
                .url(url)
                .post(body)
                .build()

        val response = client.newCall(request).execute()

        if (response.isSuccessful) {
            return true
        }

        return false
    }

    private fun fetchInfo(): String {
        val url = "http://psevents.appspot.com/api/v1/rest-auth/user/"

        val username = username_edit_text.text.toString()
        val password = password_edit_text.text.toString()



        val client = OkHttpClient()
        val request = Request.Builder()
            .url(url)
            .header("User-Agent", "Android")
            .header("Authorization",Credentials.basic("$username","$password"))
            .build()
        val response = client.newCall(request).execute()
        val bodystr = response.body().string() // this can be consumed only once

        return bodystr
    }


    // "isPasswordValid"  method goes here
    // Currently checks for 8 characters but we could perform
    // an actual validation with a remote service like the Web version below
    private fun isPasswordValid(text: Editable?): Boolean {
        return text != null && text.length >= 8
    }

    private fun isPasswordValidWeb(text: Editable?): Boolean {
        return true
    }

}
