package com.example.getappengine

import android.os.Bundle
import android.text.Editable
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.fragment.app.Fragment
import kotlinx.android.synthetic.main.activity_main.*
import kotlinx.android.synthetic.main.functions_fragment.view.*
import kotlinx.android.synthetic.main.login_fragment.*
import kotlinx.android.synthetic.main.login_fragment.view.*
import okhttp3.OkHttpClient
import okhttp3.Request
import org.jetbrains.anko.doAsync
import org.json.JSONArray

/**
 * Fragment representing the login screen for Shrine.
 */
class FunctionsFragment : Fragment() {

    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?, savedInstanceState: Bundle?): View? {
        // Inflate the layout for this fragment
        val view = inflater.inflate(R.layout.functions_fragment, container, false)

        view.findvenue.setOnClickListener {
            (activity as NavigationHost).navigateTo(VenueFragment(), false)
        }

        view.findsportcategory.setOnClickListener {
            (activity as NavigationHost).navigateTo(SportsCatFragment(), false)
        }
        view.logout.setOnClickListener {
            (activity as NavigationHost).navigateTo(LoginFragment(), false)
        }
        view.createevent.setOnClickListener {
            (activity as NavigationHost).navigateTo(CreateEventFragment(), false)
        }
        view.searcheevent.setOnClickListener {
            (activity as NavigationHost).navigateTo(SearchEventFragment(), false)
        }
        view.joinedevent.setOnClickListener {
            (activity as NavigationHost).navigateTo(JoinedEventFragment(), false)
        }

        return view
    }

    // Gets a string from the apad19 which is formatted as
    //  an Array of JSON objects: [{...},{...},...{...}]
//    private fun fetchInfo(): String {
//        val url = "https://apad19.appspot.com/list/"
//
//        val client = OkHttpClient()
//        val request = Request.Builder()
//                .url(url)
//                .header("User-Agent", "Android")
//                .build()
//        val response = client.newCall(request).execute()
//        val bodystr =  response.body().string() // this can be consumed only once
//
//        return bodystr
//    }

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
