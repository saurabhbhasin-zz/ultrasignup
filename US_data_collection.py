# US_data_collection.py

import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd

# Entrants URL for a race you're interested in
race = 'https://ultrasignup.com/entrants_event.aspx?did=51243'
csvfile = open("all_entrants.csv", "w")
writer = csv.writer(csvfile, delimiter=',')
headerrow = 'Rank', 'Age Rank', 'Projected Time', 'Age Group', 'First Name', 'Last Name', 'City', 'State'
writer.writerow(headerrow)


# Scrape entrants list and save to CSV
def entrants_to_CSV(race):
    page = requests.get(race).text
    soup = BeautifulSoup(page, 'lxml')
    all_entrants = soup.find("table", {"class": "ultra_grid"})
    for row in all_entrants.findAll('tr')[2:]:
        col = row.findAll('td')
        rank = col[0].get_text().strip()
        age_rank = col[1].get_text().strip()
        projected_time = col[3].get_text()
        ag = col[4].get_text().strip()
        fname = col[5].get_text().strip()
        lname = col[6].get_text().strip()
        city = col[7].get_text().strip()
        state = col[8].get_text().strip()
        # finishes = col[12].get_text()
        entry = rank, age_rank, projected_time, ag, fname, lname, city, state
        writer.writerow(entry)
    csvfile.close()


entrants_to_CSV(race)

# Create another file with just the names of entrants
df = pd.read_csv("all_entrants.csv")
df = df[["First Name", "Last Name"]]
df.to_csv("names.csv")
