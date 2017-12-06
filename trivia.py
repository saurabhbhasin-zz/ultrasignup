# Ask the user for the race they are interested in
# Get the race's EventID
# Then get the DateID for that EventID
# Then, look up the DistanceID (if the race has multiple distances)
# Then, look up the top 3 M and F winners for that race instance
# trivia.py

import requests
import logging

logging.basicConfig(level=logging.INFO, filename='race_trivia.log', format='%(asctime)s:%(levelname)s:%(message)s')
# DID = '41765'


def doSearch(searchstring):
    SEARCH_URL = "https://ultrasignup.com/service/events.svc/GetFeaturedEventsSearch/p=0/q=%s" % (searchstring)
    r = requests.get(SEARCH_URL)
    response = r.json()
    result_list = []
    names_list = []
    for i in response:
        row = i["eventDateId"]
        row2 = i["eventName"], i["city"], i["eventDate"], i["eventDateId"]
        names_list.append(i['eventName'])
        logging.info(row2)
        result_list.append(row)
    print(names_list)
    return result_list, names_list


def getResults():
    RESULTS_BASEURL = 'https://ultrasignup.com/service/events.svc/results/'
    URL_SUFFIX = '/json'
    result_list = doSearch("Marin")[0]
    # names_list = doSearch("Pinhoti")[1]
    # print(names_list)
    for eachid in result_list:
        url = RESULTS_BASEURL+str(eachid)+URL_SUFFIX
        r = requests.get(url)
        if r.status_code == 200:
            if r.headers['Content-Length'] == '2':
                print("No Results. Skipping")
            else:
                print("-----Getting Results. Race({})-----").format(url)
                results = r.json()
                male_athletes = []
                female_athletes = []
                for athlete in results:
                    if athlete["gender"] == "M":
                        row = ("{} {} from {} in {}".format(athlete["firstname"], athlete["lastname"], athlete["city"], athlete["formattime"]))
                        male_athletes.append(row)
                    elif athlete["gender"] == "F":
                        row = ("{} {} from {} in {}".format(athlete["firstname"], athlete["lastname"], athlete["city"], athlete["formattime"]))
                        female_athletes.append(row)
                print(male_athletes[:3])
                print(female_athletes[:3])
        else:
            logging.info("Invalid Response {}").format(r.status_code)


getResults()
