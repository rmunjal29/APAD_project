package com.example.getappengine

class CardData {
    constructor(eventId: String, eventCategory: String, venue: String, sport: String, eventName: String, eventDate: String, eventStartTime: String, eventEndTime: String, userId: String, hostFlag: String, memberFlag: String, eventDesc: String, capacityAvail: String, eventUrl: String) {
        this.eventId = eventId
        this.eventCategory = eventCategory
        this.venue = venue
        this.sport = sport
        this.eventName = eventName
        this.eventDate = eventDate
        this.eventStartTime = eventStartTime
        this.eventEndTime = eventEndTime
        this.userId = userId
        this.hostFlag = hostFlag
        this.memberFlag = memberFlag
        this.eventDesc = eventDesc
        this.capacityAvail = capacityAvail
        this.eventUrl = eventUrl
    }

    var eventId: String
    var eventCategory: String
    var venue: String
    var sport: String
    var eventName: String
    var eventDate: String
    var eventStartTime: String
    var eventEndTime: String
    var userId: String
    var hostFlag: String
    var memberFlag: String
    var eventDesc: String
    var capacityAvail: String
    var eventUrl: String
}