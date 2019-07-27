from datetime import date, timedelta
import csv
import json
import time

import requests

from config import WANTED_KURS, DAY_RANGE, SAVEFILE, PARSING_DELAY


TARGET_URL = ("https://api.exchangeratesapi.io/__date__?base=IDR"
              "&symbols={}".format(','.join(WANTED_KURS))
              )

data_list = []
today = date.today()


def response_parser(json_data):
    """
    Change a data from JSON into list.

    Structure of the list:
    [date, USD, GBP, EUR, CNY, JPY]
    """

    try:
        return [json_data.get("date")] \
               + [round(1/json_data.get("rates").get(n), 3) if n else 0 for n in WANTED_KURS ]
    except:
        print(json_data)


for day in (today - timedelta(days=n) for n in range(15)):
    if day.weekday() in [5,6]:
        continue

    response = requests.get(TARGET_URL.replace("__date__", str(day)))
    data_list.append(response_parser(response.json()))
    print(f"Parsed {str(day)}")

    time.sleep(PARSING_DELAY)


with open(SAVEFILE, "w") as data_file:
    data_writer = csv.writer(data_file,
                             delimiter=',',
                             quotechar='"',
                             quoting=csv.QUOTE_MINIMAL)

    data_writer.writerow(['Date'] + [i for i in WANTED_KURS])

    for data in data_list:
        data_writer.writerow(data)
