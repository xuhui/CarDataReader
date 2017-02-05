import urllib.request
from haversine import haversine
import json
import re

WORDS = ["EVENTS", "ROAD"]


def getPromet(lat, lon):
    # -------------------------------------------------------
    # DOBI lokacijo v obliki lat pa lon
    # VRNE bližnje dogodke kot array da jasper direkt pove
    # Link do navodil https://github.com/zejn/arsoapi
    # ---------------------------------------------------------*/
    promet = []
    range = 20 #km
    currentLocation = (lat, lon)
    link = "http://janliber.spletniki.si/"
    webPage = urllib.request.urlopen(link)
    content = webPage.read()


    events = json.loads(content.decode("utf-8"))
    for event in events:
        eventLocation = (event['lat'], event['lon'])
        distance = haversine(currentLocation, eventLocation)
        if(distance < range):
            promet.append(event["description"])


    return promet


def handle(text, mic):
    """
        Responds to user-input, typically speech text, by telling the events on the road.
        Arguments:
        text -- user-input, typically transcribed speech
        mic -- used to interact with the user (for both input and output)
    """

    lat=46.4221890
    lon=14.9262910
    events = getPromet(lat, lon)

    for event in events:
        mic.say(event)


def isValid(text):
    """
        Returns True if the input is related to events.
        Arguments:
        text -- user-input, typically transcribed speech
    """
    return bool(re.search(r'\bevents\b', text, re.IGNORECASE))