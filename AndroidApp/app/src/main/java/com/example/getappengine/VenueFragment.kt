package com.example.getappengine

import android.os.Bundle
import android.text.Editable
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.Toast
import androidx.fragment.app.Fragment
import kotlinx.android.synthetic.main.activity_main.*
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
class VenueFragment : Fragment() {

    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?, savedInstanceState: Bundle?
    ): View? {
        // Inflate the layout for this fragment
        val view = inflater.inflate(R.layout.venue_fragment, container, false)

        view.button.setOnClickListener {
            doAsync {
                val gotresponse = fetchInfo()
                val jsonarray = JSONArray(gotresponse)

                uiThread {
                    //iterate through the returned array of JSON objects
                    // and look for candiadate whose name we requested
                    for (i in 0..(jsonarray.length() - 1)) {
                        val user = jsonarray.getJSONObject(i)
                        if (user.get("venue_name") == searchvenue.text.toString()) {
                            val venue_name = user.getString("venue_name")
                            val address = user.getString("address")
                            val zip_code = user.getString("zip_code")
                            val contact_number = user.getString("contact_number")
                            val description = user.getString("description")
                            val open_time = user.getString("open_time")
                            val close_time = user.getString("close_time")
                            val games_total_count = user.getString("games_total_count")
                            val games_available_count = user.getString("games_available_count")
                            txtvenuedetails.setText(
                                "Venue Name: $venue_name\n" +
                                        "Address: $address\n" +
                                        "Zip Code: $zip_code\n" +
                                        "Contact number: $contact_number\n" +
                                        "Description: $description\n" +
                                        "Open Time: $open_time\n" +
                                        "Close Time: $close_time\n" +
                                        "Total Games: $games_total_count\n" +
                                        "Available Games: $games_available_count"
                            )
                            break
//                        (activity as NavigationHost).navigateTo(VenueFragment(), false)
                        } else {
                            txtvenuedetails.text = ""
                        }
                    }
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
        val url = "http://psevents.appspot.com/api/v1/vlv"

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