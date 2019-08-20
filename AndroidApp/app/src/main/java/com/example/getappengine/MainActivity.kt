package com.example.getappengine

import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import androidx.fragment.app.Fragment
import okhttp3.OkHttpClient
import okhttp3.Request
import kotlinx.android.synthetic.main.activity_main.*
import kotlinx.android.synthetic.main.login_fragment.*
import org.jetbrains.anko.activityUiThread
import org.jetbrains.anko.doAsync
import org.json.JSONArray
import org.json.JSONObject

class MainActivity : AppCompatActivity(), NavigationHost {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        if (savedInstanceState == null) {
            supportFragmentManager
                    .beginTransaction()
                    .add(R.id.container, LoginFragment())
                    .commit()
        }
    }


    override fun navigateTo(fragment: Fragment, addToBackstack: Boolean) {
        val transaction = supportFragmentManager
                .beginTransaction()
                .replace(R.id.container, fragment)

        if (addToBackstack) {
            transaction.addToBackStack(null)
        }

        transaction.commit()
    }
}


