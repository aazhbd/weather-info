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


@click.command()
@click.option('--cities', '-c', default='london berlin paris amsterdam', help='The list of the cities for which the weather information should be extracted. Multiple names should be put into \'..\' marks. e.g. \'berlin london paris\'')
@click.option('--output', '-o', default='forecasts', help='Name of the directory where the forecast files would be created.')
def main(cities, output):
    """
    Downloads historical weather information of different cities. To see usage, run command with --help option.
    """
    if not os.path.exists(output):
        os.makedirs(output)

    for city in cities.split():
        with open(str(output) + "/%s.json" % city, "w") as fp:
            json.dump(get_location_forecast(city), fp)
        logging.info("Downloaded forecast for %s" % city)


if __name__ == '__main__':
    main()
