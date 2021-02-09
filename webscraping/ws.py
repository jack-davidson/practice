#!/usr/bin/env python3
import requests
import json


def request_json(url):
    return json.loads(requests.get(url).text)


def main():
    satellites = request_json("https://api.wheretheiss.at/v1/satellites")

    for sat in satellites:
        if sat["name"] == "iss":
            sattelite_id = sat["id"]

    satellite = request_json(
        f"https://api.wheretheiss.at/v1/satellites/{sattelite_id}"
    )
    print(
        f"the latitude of the {satellite['name']} is {satellite['latitude']}\n"
        f"the longitude of the {satellite['name']} is {satellite['latitude']}"
    )


if __name__ == "__main__":
    main()
