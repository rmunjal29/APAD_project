package com.example.getappengine

import android.os.Bundle
import android.text.Editable
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.ArrayAdapter
import androidx.fragment.app.Fragment
import kotlinx.android.synthetic.main.activity_main.*
import kotlinx.android.synthetic.main.events_cat_fragment.*
import kotlinx.android.synthetic.main.events_cat_fragment.view.*
import kotlinx.android.synthetic.main.events_cat_fragment.view.backbutton1
import kotlinx.android.synthetic.main.joined_events_fragment.*
import kotlinx.android.synthetic.main.joined_events_fragment.view.*
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
class JoinedEventFragment : Fragment() {

    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?, savedInstanceState: Bundle?
    ): View? {
        // Inflate the layout for this fragment
        val view = inflater.inflate(R.layout.joined_events_fragment, container, false)
        doAsync {
            val gotresponse = fetchInfo()
            val jsonarray = JSONArray(gotresponse)
            //iterate through the returned array of JSON objects
            // and look for candiadate whose name we requested
            val eventNames = arrayListOf<String>()
            uiThread {
                for (i in 0..(jsonarray.length() - 1)) {
                    val user = jsonarray.getJSONObject(i)

                    val event_name = user.getString("event_name")
                    eventNames.add(event_name)

//                       (activity as NavigationHost).navigateTo(VenueFragment(), false)

                }

                view.eventlist.adapter = ArrayAdapter(activity, android.R.layout.simple_list_item_1, eventNames)
                }
            }
            view.backbutton1.setOnClickListener {
                (activity as NavigationHost).navigateTo(FunctionsFragment(), false)
            }


        return view
    }

    // Gets a string from the apad19 which is formatted as
    //  an Array of JSON objects: [{...},{...},...{...}]
    private fun fetchInfo(): String {

        val pk = Global.userid
        val url = "http://psevents.appspot.com/api/v1/jev?pk=$pk"

        val client = OkHttpClient()
        val request = Request.Builder()
            .url(url)
            .header("User-Agent", "Android")
            .build()
        val response = client.newCall(request).execute()
        val bodystr = response.body().string() // this can be consumed only once

        return bodystr
    }

}
