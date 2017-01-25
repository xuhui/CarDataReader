import time
import urllib.request
from haversine import haversine
import json

#-------------------------------------------------------
#
# Gets values from APIs
# https://opendata.si/
# Some definitions get lat and lon values
#
#---------------------------------------------------------*/


#-------------------------------------------------------
# DOBI lokacijo v obliki lat pa lon
# VRNE napoved kot string da jo jasper direkt pove
# Link do navodil https://github.com/zejn/arsoapi
#---------------------------------------------------------*/
def getVreme(lat, lon):
  napoved="Vreme bo..."
  
  
  
  
  return napoved

#-------------------------------------------------------
# DOBI lokacijo v obliki lat pa lon
# VRNE bližnje dogodke kot array da jasper direkt pove
# Link do navodil https://github.com/zejn/arsoapi
#---------------------------------------------------------*/
def getPromet(lat, lon):

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

getPromet(46.4221890,14.9262910)