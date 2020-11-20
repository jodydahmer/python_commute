import csv 

with open('teachers.csv', 'a') as csvfile:
    fieldnames = ['City', 'State', 'Average Commute']
    teachwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)

    teachwriter.writeheader()
    teachwriter.writerow({
        'City':'Atlanta ',
        'Region': 'South',
        'Commute Time': '30'
    })