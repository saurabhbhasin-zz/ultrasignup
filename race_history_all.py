import csv


from race_history_individual import get_athlete_races


def get_all_history():
    with open("names.csv", "r") as f:
        csv_reader = csv.reader(f, delimiter=",")
        for row in csv_reader:
            fname = (row[1])
            lname = (row[2])
            fullname = fname + lname
            print(fullname)
            get_athlete_races(fname, lname)


def main():
    get_all_history()


if __name__ == '__main__':
    main()
