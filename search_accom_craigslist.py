#!/usr/bin/python

''' pip install python-craigslist
 https://pypi.org/project/python-craigslist/

 pip install python-googlegeocoder
'''
from craigslist import CraigslistHousing
import os
import csv
import pandas as pd

count = 0

def main():
    search_and_write_to_csv()
    #remove_duplicate_rows_from_csv()


def search_and_write_to_csv():
    # for loop taking in the defined zip codes, if not set, use a default list
    # default list could be the zip codes of each underground station
    yellow_lines = {
        "LAWRENCE": "M4N 1S1",
        "EGLINTON": "M4S 2B8",
        "DAVISVILLE": "M4S 1Z2"
    }

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


    for station in yellow_line:
        zip_code = yellow_line[station]
        search_distance = 1.5
        max_price = 2500
        cl_h = CraigslistHousing(site='toronto', area='tor', category='apa',
                             filters={'zip_code':zip_code,'search_distance':search_distance,
                                      'posted_today':True,'has_image':True,'max_price': max_price
                                      })
        results = cl_h.get_results(sort_by='newest', geotagged=True)
        write_results_of_search_to_csv(results, station)



def write_results_of_search_to_csv(results, station):

    cwd = os.getcwd()
    file_name = cwd + '/results.csv'

    results_data = open(file_name, 'a', newline='')
    # a is open for writing/append if already exists
    csvwriter = csv.writer(results_data)

    print("Processing", station)

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
            csvwriter.writerow(header)
            count += 1
        

        csvwriter.writerow(result.values())

    results_data.close()

def remove_duplicate_rows_from_csv():
    print("Removing duplicates from csv")
    cwd = os.getcwd()
    file_name = cwd + '/results.csv'
    df = pd.read_csv(file_name)
    # dropping duplicates based on name and url columns
    df.drop_duplicates(subset=['name','url'], keep='first', inplace=True)
    df.to_csv(cwd + '/results.csv')



if __name__ == "__main__":
    main()
