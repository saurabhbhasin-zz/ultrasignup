import requests
import csv
import logging
from convert import getLat, getLng, getAddress

logging.basicConfig(level=logging.INFO, filename='races.log')


def lambda_handler(zipcode, dist_code):
    url = "https://ultrasignup.com/service/events.svc/closestevents?past=0&lat=%s&lng=%s&mi=300&mo=12&on&dist=%s" % (lat, lng, dist_code)
    # logging.info(url)
    r = requests.get(url)
    response = r.json()
    number_of_races = "found %s races" % len(response)
    logging.info(number_of_races)
    logging.info(address)
    csvfile = open("upcoming_races.csv", "w")
    writer = csv.writer(csvfile, delimiter=',')
    headerrow = 'EventDate', 'EventName', 'City', 'Distances', 'Event ID', 'Event Date ID'
    writer.writerow(headerrow)
    for i in response:
        row = i["EventDate"], i["EventName"], i["City"], i["Distances"], i["EventId"], i["EventDateId"]
        writer.writerow(row)
        # print(i)
    return response


zipcode = input("Enter Zipcode: ")
dist_code = input("Distance Code (100M = 7, 100K = 6, 50M = 5): ")
lat = getLat(zipcode)
lng = getLng(zipcode)
address = getAddress(zipcode)
lambda_handler(zipcode, dist_code)
