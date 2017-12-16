# Get the race's EventID
# Then get the DateID for that EventID
# Then, look up the DistanceID (if the race has multiple distances)
# Then, look up the top 3 M and F winners for that race instance
# trivia.py

import requests
import logging

logging.basicConfig(level=logging.INFO, filename='race_trivia.log',
                    format='%(asctime)s:%(levelname)s:%(message)s')


def doSearch(searchstring):
    SEARCH_URL = "https://ultrasignup.com/service/events.svc/GetFeaturedEventsSearch/p=0/q=%s" % (searchstring)
    r = requests.get(SEARCH_URL)
    response = r.json()
    result_list = []
    for i in response:
        row = i["eventDateId"]
        result_list.append(row)
        row2 = i["eventName"], i["city"], i["eventDate"], i["eventDateId"]
        logging.info(row2)
    return result_list


def getResults():
    RESULTS_BASEURL = 'https://ultrasignup.com/service/events.svc/results/'
    URL_SUFFIX = '/json'
    result_list = doSearch("Whistle")
    for eachid in result_list:
        url = RESULTS_BASEURL+str(eachid)+URL_SUFFIX
        r = requests.get(url)
        if r.status_code == 200:
            if r.headers['Content-Length'] == '2':
                print("No Results for {}. Skipping".format(eachid))
            else:
                print("-----Found results for race ({})-----").format(url)
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


# def geteventName(searchstring):
#     SEARCH_URL = "https://ultrasignup.com/service/events.svc/GetFeaturedEventsSearch/p=0/q=%s" % (searchstring)
#     r = requests.get(SEARCH_URL)
#     response = r.json()
#     names_list = []
#     for i in response:
#         names_list.append(i['eventName'])
#     print(names_list)
#     return names_list
