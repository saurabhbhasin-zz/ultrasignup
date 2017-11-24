# race_history_individual.py
import requests
import csv
import logging
# import pandas as pd
# import matplotlib.pyplot as plt
logging.basicConfig(level=logging.INFO, filename='race_history.log')


# get relevant data and write to file
def get_athlete_races(fname, lname):
    url = 'https://ultrasignup.com/service/events.svc/history/%s/%s' % (fname,
                                                                        lname)
    file_name = fname + '_' + lname + '.csv'
    results = requests.get(url)
    athlete_json = results.json()
    with open(file_name, 'w', encoding='utf-8') as target:
        writer = csv.writer(target, delimiter=",")
        writer.writerow(["Event", "Event Date", "Finish Time", "Place",
                        "Gender Place", "Rank"])
        for i in athlete_json:
            for results in i['Results']:
                eventname = results.get('eventname')
                eventdate = results.get('eventdate')
                place = results.get('place')
                gender_place = results.get('gender_place')
                rank = results.get('runner_rank')
                time = results.get('time')
                row = eventname, eventdate, time, place, gender_place, rank
                writer.writerow(row)


def main():
    # ask for name
    fname = input('Enter athlete first name:')
    lname = input('Enter athlete last name:')
    get_athlete_races(fname, lname)


if __name__ == '__main__':
    main()
