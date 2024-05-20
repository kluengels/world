### open countries object from file system or fetch and open

from pathlib import Path
import requests # http requests
import json # work with json data
import sys

def get_countries():
    # if json-data is not in parent dir, fetch it from API
    if not (Path.cwd() / "countries.json").is_file():
        try:
            # fetch country data
            r = requests.get("https://restcountries.com/v3.1/all", timeout=30) #?fields=name,flag,capital,flags
            raw = json.loads(r.text)
            json_object = json.dumps(raw, indent=4)

            # write to file
            with open("countries.json", "w") as file:
                file.write(json_object)
            r.raise_for_status()
            
        # error handling
        except:
            sys.exit("Could not fetch countries from API, please restart")
        

    # Open json-data saved locally
    try:
        f = open("countries.json", "r")
        return json.load(f)
    except:
        sys.exit("Could not open the file countries.json")
