import json

import requests
import time
import datetime



def getData(id):
    token = "d06fe9af7943c4c3707aa4c94a5ecf24"
    url = "https://api.stlouisfed.org/fred/series/observations?series_id="+id+"&api_key="+token+"&file_type=json&frequency=m&realtime_start=2020-01-01"
    return requests.get(url).json();



result = getData("UNRATE")

with open("Output.txt", "w") as text_file:
    text_file.write(json.dumps(result))
print(result)

