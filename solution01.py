import click
import logging
import os
import sys
import requests
import json


def get_location_forecast(location):
    loc_resp = requests.get(
        "https://www.metaweather.com/api/location/search/",
        params=dict(query=location)
    )
    loc_woeid = loc_resp.json()[0]["woeid"]

    print("City: " + str(location) + " : " + str(loc_woeid))

    forecast_resp = requests.get(
        "https://www.metaweather.com/api/location/%s/" % loc_woeid
    )
    forecast_resp.raise_for_status()
    return forecast_resp.json().get("consolidated_weather")
