#!/usr/bin/python

''' pip install python-craigslist
 https://pypi.org/project/python-craigslist/

 pip install pandas

'''
from craigslist import CraigslistHousing
import os
import csv
import pandas as pd
import datetime

count = 0
cwd = os.getcwd()
daily_csv_file_name = cwd + '/'+datetime.datetime.today().strftime('%Y-%m-%d')+'-results.csv'
total_csv_file_name = cwd + '/total_results.csv'

def main():
    search_and_write_to_csv()
    remove_duplicate_rows_from_csv()


def search_and_write_to_csv():
    # for loop taking in the defined zip codes, if not set, use a default list
    # default list could be the zip codes of each underground station

    # west to east starting Dundas West
    green_line = {
        "DUNDAS WEST": "M6P 1W7",
        "DUFFERIN": "M6H 4E6",
        "CHRISTIE": "M6G 3B1",
        "BAY": "M5R 3N7"
    }

    # north east to south to north west
    yellow_line = {
        "LAWRENCE": "M4N 1S1",
        "EGLINTON": "M4S 2B8",
        "DAVISVILLE": "M4S 1Z2",
        "ST CLAIR": "M4T 1J8",
        "SUMMERHILL": "M4T 1W2",
        "ROSEDALE": "M4W 1T1",
        "BLOOR-YONGE": "M4W 1A8",
        "WELLESLEY": "M4Y 1G3",
        "COLLEGE": "M5B 1L2",
        "DUNDAS": "M5G 1Z3",
        "QUEEN": "M5C 2X9",
        "KING": "M5H 1A1",
        "UNION": "M5J 1E6",
        "ST ANDREW": "M5H 3T4",
        "OSGOODE": "M5H 3E5",
        "ST PATRICK": "M5G 1V1",
        "QUEENS PARK": "M5G 1X7",
        "MUSEUM": "M5S 2C5",
        "ST GEORGE": "M5R 2L8",
        "SPADINA": "M5R 2T6",
        "DUPONT": "M5R 1V7",
        "ST CLAIR WEST": "M5P 3N3"
    }

    lines = [green_line, yellow_line]

    for line in lines:
        print("Processing", line)
        for station in line:
            zip_code = line[station]
            search_distance = 1.5
            max_price = 2500
            cl_h = CraigslistHousing(site='toronto', area='tor', category='apa',
                                filters={'zip_code':zip_code,'search_distance':search_distance,
                                        'posted_today':True,'has_image':True,'max_price': max_price
                                        })
            results = cl_h.get_results(sort_by='newest', geotagged=True)
            write_results_of_search_to_csv(results, station)



def write_results_of_search_to_csv(results, station):

    with open (daily_csv_file_name, 'a', newline='', encoding="utf-8") as daily_csv_file, open (total_csv_file_name, 'a', newline='',  encoding="utf-8") as total_csv_file:
        daily_csv_file_writer = csv.writer(daily_csv_file)
        total_csv_file_writer = csv.writer(total_csv_file)

        # a is open for write/append if already exists

        print("\tProcessing", station)

        for result in results:
            # removing unnecessary info
            del result["id"]
            del result["repost_of"]
            del result["has_image"]
            del result["has_map"]

            # adding the station into the result
            result["Station"] = station

            # writing in header row only the first time
            global count
            if count == 0:
                header = result.keys()
                daily_csv_file_writer.writerow(header)
                total_csv_file_writer.writerow(header)
                count += 1


            daily_csv_file_writer.writerow(result.values())
            total_csv_file_writer.writerow(result.values())
        
        daily_csv_file.close()
        total_csv_file.close()

def remove_duplicate_rows_from_csv():
    print("Removing duplicates from csv")
    csv_files = [daily_csv_file_name, total_csv_file_name]

    for csv_file in csv_files:
        df = pd.read_csv(csv_file)
        # dropping duplicates based on name and url columns
        df.drop_duplicates(subset=['name','url'], keep='first', inplace=True)
        df.to_csv(csv_file)


if __name__ == "__main__":
    main()
