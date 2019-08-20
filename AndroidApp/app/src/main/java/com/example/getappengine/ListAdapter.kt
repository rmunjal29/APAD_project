package com.example.getappengine

import android.content.Context;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.BaseAdapter
import kotlinx.android.synthetic.main.event_card_fragment.view.*
import okhttp3.MediaType
import okhttp3.OkHttpClient
import okhttp3.Request
import okhttp3.RequestBody
import org.json.JSONArray

class ListAdapter(var eventList: ArrayList<CardData>, var context: Context) : BaseAdapter() {

    private val inflater: LayoutInflater
            = context.getSystemService(Context.LAYOUT_INFLATER_SERVICE) as LayoutInflater

    override fun getView(position: Int, convertView: View?, parent: ViewGroup?): View {
        val view = inflater.inflate(R.layout.event_card_fragment, parent, false)

        view.cardeventid.setOnClickListener {
            val url1 = eventList[position].eventUrl

            val v0 = eventList[position].eventId
            val v1 = eventList[position].eventCategory
            val v2 = eventList[position].sport
            val v3 = eventList[position].venue
            val v4 = eventList[position].eventName
            val v5 = eventList[position].eventDate
            val v6 = eventList[position].eventStartTime
            val v7 = eventList[position].eventEndTime
            val v8 = eventList[position].userId
            val v9 = eventList[position].hostFlag
            val v10 = eventList[position].memberFlag
            val v11 = eventList[position].eventDesc
            val v12 = eventList[position].capacityAvail


            val json = """
            {
                "event_name":"$v4",
                "event_date":"$v5",
                "start_time":"$v6",
                "end_time":"$v7",
                "member_flag":"1",
                "capacity_avail":"$v12"
            }
            """.trimIndent()

            if (joinreq(url1, json)){

                view.joinmessage.setText( "You have successfully joined the event")

            }

            else{

                view.joinmessage.setText("You have already joined the event")

            }

//            println("Hello")
        }


        view.joinmessage.text = eventList[position].eventUrl
        view.cardeventname.text = eventList[position].eventName
        view.cardeventdate.text = eventList[position].eventDate
        view.cardeventstarttime.text = eventList[position].eventStartTime
        view.cardeventendtime.text = eventList[position].eventEndTime



        return view
    }

    override fun getItem(position: Int): Any {
        return eventList[position]
    }

    override fun getItemId(position: Int): Long {
        return position.toLong()
    }

    override fun getCount(): Int {
        return eventList.size
    }

    private fun joinreq(url:String, json:String): Boolean {



        val body = RequestBody.create(MediaType.parse("application/json; charset=utf-8"), json)

        val client = OkHttpClient()
        val request = Request.Builder()
            .url(url)
            .put(body)
            .build()

        val response = client.newCall(request).execute()

        if (response.isSuccessful) {
            return true
        }

        return false
    }


}