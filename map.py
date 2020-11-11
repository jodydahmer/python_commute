#This is the first thing I am doing using Python! Hello World!
#



# Ideas
# I want to eventually put this 
#Scooters - Lou Metro Open Data
#Map Data Google Maps KSV Export
#Tweepy and pandas using keyword "commute"
commute_time=2
def Commute():
    commute_time = input("Please enter your commute time in minutes to work!")
    attempt_count = 1
    while commute_time == ("") or type(commute_time) !=int:
        if attempt_count > 2:
            sys.exit("It's ok, try another number!")
        attempt_count += 1
    print("Your commute time is ",commute_time,"!")
Commute()




##Hours_remaining -= daily_commute



#Make an list showing average commute times of cities

#City
#Commute in Minutes (*60 for hours)
#Region of US


#Chicago_commute = 
#["
    #"Chicago"
    #"30"
    #"Midwest"

