package com.example.getappengine

import android.os.Bundle
import android.text.Editable
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.AdapterView
import android.widget.ArrayAdapter
import android.widget.Spinner
import android.widget.Toast
import androidx.fragment.app.Fragment
import kotlinx.android.synthetic.main.activity_main.*
import kotlinx.android.synthetic.main.create_event_fragment.*
import kotlinx.android.synthetic.main.login_fragment.*
import kotlinx.android.synthetic.main.login_fragment.view.*
import kotlinx.android.synthetic.main.login_fragment.view.next_button
import kotlinx.android.synthetic.main.venue_fragment.*
import kotlinx.android.synthetic.main.venue_fragment.view.*
import okhttp3.MediaType
import okhttp3.OkHttpClient
import okhttp3.Request
import okhttp3.RequestBody
import org.jetbrains.anko.doAsync
import org.jetbrains.anko.uiThread
import org.json.JSONArray
import java.util.ArrayList

/**
 * Fragment representing the login screen for Shrine.
 */
class CreateEventFragment : Fragment() {

    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?, savedInstanceState: Bundle?): View? {
        // Inflate the layout for this fragment
        val view = inflater.inflate(R.layout.create_event_fragment, container, false)

        var venuelist:List<VenueModel> = getEventCat()
        var venuenamelist = mutableListOf<String>()
        venuelist.forEach() {
            venuenamelist.add(it.venueName!!)
        }
        val adapter = ArrayAdapter(requireContext(), android.R.layout.simple_spinner_item, venuenamelist)
        adapter.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item)
        val venueSpinner: Spinner = view.findViewById(R.id.venueSpinner)
        venueSpinner.adapter = adapter
        venueSpinner.onItemSelectedListener = object: AdapterView.OnItemSelectedListener {
            override fun onNothingSelected(parent: AdapterView<*>?) {
            }
            override fun onItemSelected(parent: AdapterView<*>, view: View?, position: Int, id: Long) {
                val item = adapter.getItem(position)
            }
        }

        view.button.setOnClickListener {
            val venue = venueSpinner.getSelectedItem().toString()
            val venue_id = getVenueId(venue,venuelist)
            val event_category_1 = eventcat.text.toString()
            val sports_category_1 = sportscat.text.toString()
            val event_name_1 = eventname.text.toString()
            val event_date_1 = eventdate.text.toString()
            val start_time_1 =  eventstarttime.text.toString()
            val end_time_1 =  eventendtime.text.toString()
            val user_id_1 =  Global.userid
            val event_desc_1 = eventdesc.text.toString()
            val capacity_available_1 = capavail.text.toString()
            val jason_event_data = """
                {
                    "event_category":"$event_category_1",
                    "sport":"$sports_category_1",
                    "venue":"$venue_id",
                    "event_name":"$event_name_1",
                    "event_date":"$event_date_1",
                    "start_time":"$start_time_1",
                    "end_time":"$end_time_1",
                    "user_id":"$user_id_1",
                    "host_flag":"1",
                    "member_flag":"0",
                    "event_desc":"$event_desc_1",
                    "capacity_avail":"$capacity_available_1"
                }
                """.trimIndent()

            if (createvent(jason_event_data)){
                (activity as NavigationHost).navigateTo(FunctionsFragment(), false)

            }

        }


        view.backbutton.setOnClickListener{
            (activity as NavigationHost).navigateTo(FunctionsFragment(), false)
        }

        return view
    }

    // Gets a string from the apad19 which is formatted as
    //  an Array of JSON objects: [{...},{...},...{...}]
    private fun createvent(json: String): Boolean {
        val url = "http://psevents.appspot.com/api/v1/elv/"


        val client = OkHttpClient()

        val body = RequestBody.create(MediaType.parse("application/json; charset=utf-8"), json)
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

    private fun getEventCat(): List<VenueModel> {
        val url = "http://psevents.appspot.com/api/v1/vlv"

        val client = OkHttpClient()
        val request = Request.Builder()
            .url(url)
            .header("User-Agent", "Android")
            .build()
        val response = client.newCall(request).execute()
        val bodystr = response.body().string() // this can be consumed only once

        var arr = ArrayList<VenueModel>()

        val jsonarray = JSONArray(bodystr)

        for (i in 0..(jsonarray.length() - 1)) {
            val user = jsonarray.getJSONObject(i)

            var venue = VenueModel()

            venue.venueId = user.getString("id")
            venue.venueName = user.getString("venue_name")

            arr.add(venue)

        }

        return arr
    }

        private fun getVenueId(venue: String, venuelist: List<VenueModel>) :String?{
            var venue_id:String? = ""

            venuelist.forEach(){
                if (venue==it.venueName){
                    venue_id = it.venueId
                }
            }
            return venue_id
        }


}
