# 2016 Stuff
import requests
from statistics import median

url2016 = 'https://ultrasignup.com/service/events.svc/results/35456/json?_search=false&nd=1508212876228&rows=1500&page=1&sidx=status+asc%2C+&sord=asc'
response2016 = requests.get(url2016)
results = response2016.json()

age2 = []
ftime = []
for i in results:
    age2.append(i["age"])
    ftime.append(i["formattime"])
print("The median age of athletes at RDL100 2016 was:")
print(median(age2))
print("The median finish time of athletes at RDL100 2016 was:")
print(median(ftime))
