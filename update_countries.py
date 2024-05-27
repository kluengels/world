### function to manually update countries.json file


import requests  # http requests
import json  # work with json data
import sys


def main():
    # fetch json data from from API
    try:
        # fetch country data
        print("Fetching countries data")
        r = requests.get(
            "https://restcountries.com/v3.1/all?fields=name,capital,flags,borders,population,area,region,cca3",
            timeout=120,
        )  # ?fields=name,capital,flags,borders,population,area,region,cca3
        raw = json.loads(r.text)
        json_object = json.dumps(raw, indent=4)


        # write to file
        with open("countries.json", "w") as file:
            file.write(json_object)
        r.raise_for_status()
        print("Countries data updated")

    # error handling
    except:
        sys.exit(
            "Could not fetch countries from API, please make sure you are connected to the internet and restart"
        )


if __name__ == "__main__":
    main()
