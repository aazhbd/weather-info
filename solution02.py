import click
import logging
import os
import sys
import requests
import json


def get_location_forecast(location, year, month, day):
    loc_resp = requests.get(
        "https://www.metaweather.com/api/location/search/", params=dict(query=location))
    loc_woeid = loc_resp.json()[0]["woeid"]

    forecast_resp = requests.get(
        "https://www.metaweather.com/api/location/{}/{}/{}/{}".format(loc_woeid, year, month, day))
    forecast_resp.raise_for_status()
    return forecast_resp.json()


def find_temperature_difference(city1, city2):
    city1_length = len(city1)
    city2_length = len(city2)

    if city1_length != city2_length or city1_length == 0 or city2_length == 0:
        click.echo("Received data is not valid, and processing could not be continued.")
        return

    diffs = []
    total_diff = {}

    for i in range(city2_length):
        try:
            total_diff['city1_the_temp'] = float(city1[i]['the_temp'])
            total_diff['city2_the_temp'] = float(city2[i]['the_temp'])
            total_diff['the_diff'] = float(
                city1[i]['the_temp']) - float(city2[i]['the_temp'])

            total_diff['city1_min_temp'] = float(city1[i]['min_temp'])
            total_diff['city2_min_temp'] = float(city2[i]['min_temp'])
            total_diff['min_diff'] = float(
                city1[i]['min_temp']) - float(city2[i]['min_temp'])

            total_diff['city1_max_temp'] = float(city1[i]['max_temp'])
            total_diff['city2_max_temp'] = float(city2[i]['min_temp'])
            total_diff['max_diff'] = float(
                city1[i]['max_temp']) - float(city2[i]['max_temp'])
        except:
            click.echo("Received data is not valid, and processing could not be continued.")
            return

        diffs.append(total_diff)

    return diffs



@click.command()
@click.argument('start_year', default=2014, nargs=1)
@click.argument('end_year', default=2018, nargs=1)
@click.option('--output', '-o', default='forecast_diffs', help='Name of the directory where the forecast files would be created.')
def main(start_year, end_year, output):
    """
    Downloads historical weather information of Rio and London, within a range of year. To see usage, run command with --help option.
    """
    if not os.path.exists(output):
        os.makedirs(output)

    if start_year >= end_year and end_year < 2018:
        click.echo("Year range is not valid.")
        return

    for year in range(start_year, end_year+1):
        print("resolving year : ", year)
        rio = get_location_forecast('rio', year, 4, 30)
        london = get_location_forecast('london', year, 4, 30)
        info = find_temperature_difference(rio, london)
        
        if info:
            with open(str(output) + "/diff-%s.json" % str(year), "w") as fp:
                json.dump(info, fp)
            logging.info("Saved forecast difference for year: %s" % year)



if __name__ == '__main__':
    main()
