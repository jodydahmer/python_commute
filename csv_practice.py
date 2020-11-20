import csv

with open('cities_commute.csv' , newline='') as csvfile:
    artreader = csv.reader(csvfile)
    rows = list(artreader)
    for row in rows[:4]:
        print(', '.join(row))

with open('cities_commute.csv' , newline='') as csvfile:
    artreader = csv.DictReader(csvfile)
    rows = list(artreader)
    for row in rows[1:4]:
        print(row['group1'])