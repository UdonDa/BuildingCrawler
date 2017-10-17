# cofing:utf-8
"""
Google Places API https://developers.google.com/places/
key: AIzaSyBcyTZYxBbc7-OIYx3EmsZDYY5Qg4jh0Nc


"""
import sys,os
sys.path.append("./")
from src.keyHolder.keyHolder import apiKey
from googleplaces import *

APIKEY = apiKey()
google_places = GooglePlaces(APIKEY)
query_result = google_places.nearby_search(
    location="横浜",
    keyword="ローソン",
    radius="2000",
    types=""

)

class PlacesCrawler():
    def __init__(self):
        pass



