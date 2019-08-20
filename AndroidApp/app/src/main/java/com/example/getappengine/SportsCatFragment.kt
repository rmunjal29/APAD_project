package com.example.getappengine

import android.os.Bundle
import android.text.Editable
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.fragment.app.Fragment
import kotlinx.android.synthetic.main.sports_cat_fragment.*
import kotlinx.android.synthetic.main.sports_cat_fragment.view.*
import okhttp3.OkHttpClient
import okhttp3.Request
import org.jetbrains.anko.doAsync
import org.jetbrains.anko.uiThread
import org.json.JSONArray

/**
 * Fragment representing the login screen for Shrine.
 */
class SportsCatFragment : Fragment() {

    override fun onCreateView(
            inflater: LayoutInflater, container: ViewGroup?, savedInstanceState: Bundle?): View? {
        // Inflate the layout for this fragment
        val view = inflater.inflate(R.layout.sports_cat_fragment, container, false)

        view.button2.setOnClickListener {
            doAsync {
                val gotresponse = fetchInfo()
                val jsonarray = JSONArray(gotresponse)
                uiThread {
                    //iterate through the returned array of JSON objects
                    // and look for candiadate whose name we requested
                    for (i in 0..(jsonarray.length() - 1)) {
                        val user = jsonarray.getJSONObject(i)
                        if (user.get("sport_name") == searchsportscat.text.toString()) {
                            val sport_name = user.getString("sport_name")
                            val player_count = user.getString("player_count")
                            val equip_req_flag = user.getString("equip_req_flag")
                            val sport_desc = user.getString("sport_desc")
                            txtsportscatdetails.text = "$sport_name , $player_count , $equip_req_flag , $sport_desc"
                            break
//                        (activity as NavigationHost).navigateTo(VenueFragment(), false)
                        } else {
                            txtsportscatdetails.text = ""
                        }
                    }
                }
            }
        }
        view.backbutton2.setOnClickListener{
            (activity as NavigationHost).navigateTo(FunctionsFragment(), false)
        }

        return view
    }

    // Gets a string from the apad19 which is formatted as
    //  an Array of JSON objects: [{...},{...},...{...}]
    private fun fetchInfo(): String {
        val url = "http://psevents.appspot.com/api/v1/sv"

        val client = OkHttpClient()
        val request = Request.Builder()
                .url(url)
                .header("User-Agent", "Android")
                .build()
        val response = client.newCall(request).execute()
        val bodystr =  response.body().string() // this can be consumed only once

        return bodystr
    }



}
