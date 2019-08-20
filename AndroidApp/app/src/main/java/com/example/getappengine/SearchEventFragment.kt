package com.example.getappengine

import android.os.Bundle
import android.text.Editable
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.ArrayAdapter
import androidx.core.view.isVisible
import androidx.fragment.app.Fragment
import kotlinx.android.synthetic.main.create_event_fragment.eventdate
import kotlinx.android.synthetic.main.create_event_fragment.eventendtime
import kotlinx.android.synthetic.main.create_event_fragment.eventstarttime
import kotlinx.android.synthetic.main.create_event_fragment.view.*
import kotlinx.android.synthetic.main.login_fragment.view.next_button
import kotlinx.android.synthetic.main.search_event_fragment.*
import kotlinx.android.synthetic.main.search_event_fragment.view.*
import kotlinx.android.synthetic.main.search_event_fragment.view.eventdate
import kotlinx.android.synthetic.main.venue_fragment.view.*
import kotlinx.android.synthetic.main.venue_fragment.view.backbutton
import okhttp3.MediaType
import okhttp3.OkHttpClient
import okhttp3.Request
import okhttp3.RequestBody
import org.jetbrains.anko.doAsync
import org.jetbrains.anko.uiThread
import org.json.JSONArray

/**
 * Fragment representing the login screen for Shrine.
 */
class SearchEventFragment : Fragment() {

    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?, savedInstanceState: Bundle?
    ): View? {
        // Inflate the layout for this fragment
        val view = inflater.inflate(R.layout.search_event_fragment, container, false)

        view.followbutton.setOnClickListener {
            doAsync {
                val gotresponse = fetchInfo()
                val jsonarray = JSONArray(gotresponse)

                uiThread {
                    val eventArrayList = arrayListOf<CardData>()
                    for (i in 0..(jsonarray.length() - 1)) {
                        val user = jsonarray.getJSONObject(i)

                        val event_id = user.getString("id")
                        val url = "http://psevents.appspot.com/api/v1/elv/$event_id/"

                        val eventCard = CardData(
                            user.getString("id"),
                            user.getString("event_category"),
                            user.getString("venue"),
                            user.getString("sport"),
                            user.getString("event_name"),
                            user.getString("event_date"),
                            user.getString("start_time"),
                            user.getString("end_time"),
                            user.getString("user_id"),
                            user.getString("host_flag"),
                            user.getString("member_flag"),
                            user.getString("event_desc"),
                            user.getString("capacity_avail"),
                            "$url"
                        )



                        eventArrayList.add(eventCard)
                    }

                    //make other elements invisible
                    //TODO - can also just navigate to another fragment
                    eventdate.isVisible = false
                    eventstarttime.isVisible = false
                    eventendtime.isVisible = false
                    zipcode.isVisible = false
                    followbutton.isVisible = false

                    view.eventlist.adapter = ListAdapter(eventArrayList, context!!)

                }

            }
        }
        view.backbutton.setOnClickListener {
            (activity as NavigationHost).navigateTo(FunctionsFragment(), false)
        }

        return view
    }

    // Gets a string from the apad19 which is formatted as
    //  an Array of JSON objects: [{...},{...},...{...}]
    private fun fetchInfo(): String {
        val event_date_1 = eventdate.text.toString()
        val start_time_1 = eventstarttime.text.toString()
        val end_time_1 = eventendtime.text.toString()
        val zip_code_1 = zipcode.text.toString()
        val jason_evt_data_url =
            """http://psevents.appspot.com/api/v1/elv?event_date=$event_date_1&start_time=$start_time_1&end_time=$end_time_1&zip_code=$zip_code_1"""
        println(jason_evt_data_url)

        val client = OkHttpClient()
        val request = Request.Builder()
            .url(jason_evt_data_url)
            .header("User-Agent", "Android")
            .build()
        val response = client.newCall(request).execute()
        val bodystr = response.body().string() // this can be consumed only once
        return bodystr
    }



//        val request = Request.Builder()
//                .url(url)
//                .header("User-Agent", "Android")
//                .build()
//        val response = client.newCall(request).execute()
//        val bodystr =  response.body().string() // this can be consumed only once
//


//        val body = RequestBody.create(MediaType.parse("application/json; charset=utf-8"), jason_evt_data)
//        val request1 = Request.Builder()
//                .url(url1)
//                .post(body)
//                .build()
//
//        val response1 = client.newCall(request1).execute()
//        return response1.body().string()
    }



