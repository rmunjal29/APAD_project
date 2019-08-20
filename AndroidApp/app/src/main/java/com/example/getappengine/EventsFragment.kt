package com.example.getappengine

import android.os.Bundle
import android.text.Editable
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.fragment.app.Fragment
import kotlinx.android.synthetic.main.activity_main.*
import kotlinx.android.synthetic.main.events_fragment.*
import kotlinx.android.synthetic.main.events_fragment.view.*
import kotlinx.android.synthetic.main.login_fragment.*
import kotlinx.android.synthetic.main.login_fragment.view.*
import kotlinx.android.synthetic.main.login_fragment.view.next_button
import kotlinx.android.synthetic.main.venue_fragment.*
import kotlinx.android.synthetic.main.venue_fragment.view.*
import okhttp3.OkHttpClient
import okhttp3.Request
import org.jetbrains.anko.doAsync
import org.jetbrains.anko.uiThread
import org.json.JSONArray

/**
 * Fragment representing the login screen for Shrine.
 */
class EventsFragment : Fragment() {

    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?, savedInstanceState: Bundle?): View? {
        // Inflate the layout for this fragment
        val view = inflater.inflate(R.layout.events_fragment, container, false)

        view.button3.setOnClickListener {
            doAsync {
                val gotresponse = fetchInfo()
                val jsonarray = JSONArray(gotresponse)
                uiThread {
                    //iterate through the returned array of JSON objects
                    // and look for candiadate whose name we requested
                    for (i in 0..(jsonarray.length() - 1)) {
                        val user = jsonarray.getJSONObject(i)
                        if (user.get("event_name") == searchevent.text.toString()) {
                            val event_category = user.getString("event_category")
                            val sport = user.get("sport").toString()
                            val venue = user.get("venue").toString()
                            val event_name = user.get("event_name").toString()
                            val event_date = user.get("event_date").toString()
                            val start_time = user.get("start_time").toString()
                            val end_time = user.get("end_time").toString()
                            val event_desc = user.get("event_desc").toString()
                            val capacity_avail = user.get("capacity_avail").toString()
                            txteventdetails.text = "$event_category , $sport , $venue , $event_name , $event_date , $start_time , $end_time , $event_desc , $capacity_avail "
                            break
//                        (activity as NavigationHost).navigateTo(VenueFragment(), false)
                        } else {
                            txteventdetails.text = ""
                        }
                    }
                }
            }
        }
        view.backbutton3.setOnClickListener{
            (activity as NavigationHost).navigateTo(FunctionsFragment(), false)
        }

        return view
    }

    // Gets a string from the apad19 which is formatted as
    //  an Array of JSON objects: [{...},{...},...{...}]
    private fun fetchInfo(): String {
        val url = "http://psevents.appspot.com/api/v4/?format=json"

        val client = OkHttpClient()
        val request = Request.Builder()
                .url(url)
                .header("User-Agent", "Android")
                .build()
        val response = client.newCall(request).execute()
        val bodystr =  response.body().string() // this can be consumed only once

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
