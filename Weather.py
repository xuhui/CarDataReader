import urllib.request
from haversine import haversine
import json



import urllib.request
from haversine import haversine
import json
import re

WORDS = ["WEATHER"]


def getVreme(lat, lon):
    link = "https://opendata.si/vreme/report/?lat=" + str(lat) + "&lon=" + str(lon)
    webPage = urllib.request.urlopen(link)
    content = webPage.read()

    weather = json.loads(content.decode("utf-8"))
    weather = weather['forecast']['data'][0]


    weatherString = "Weather forecast for the next "+ str(weather['offset']) + " hours. "
    weatherString = weatherString + "Clouds percentage: " + str(weather['clouds']) + "."
    weatherString = weatherString + " Rain probability: " + str(weather['rain'] + ".")

    return weatherString



def handle(text, mic):
    """
        Responds to user-input, typically speech text, by telling the events on the road.
        Arguments:
        text -- user-input, typically transcribed speech
        mic -- used to interact with the user (for both input and output)
    """

    lat=46.4221890
    lon=14.9262910
    weatherReport = getVreme(lat, lon)


    mic.say(weatherReport)


def isValid(text):
    """
        Returns True if the input is related to events.
        Arguments:
        text -- user-input, typically transcribed speech
    """
    return bool(re.search(r'\bweather\b', text, re.IGNORECASE))