#National Average of CommuteTimes 
NATIONAL_AVERAGE = 30
#This application will take user input for their average one way commute time , compare it to a list of commute times for other cities , then use functions to determine if the user inputted commute time was larger or smaller than the US average. 
import math
from datetime import date, time, datetime


#This year has been really hard on me, so I used a 2020 countdown clock as a way to feature datetime
#FEATURE datetime is used to get current date and determine what the current year is, current month is to make calculations based on the timedelta

date_format = "%m/%d/"
now = datetime.now()
new_year = datetime(now.year, 12, 31)
delta = new_year - now
final = delta.days


today = date.today()
current_date = datetime.now().date()
current_year = current_date.year
current_month = current_date.month


#FEATURE Create and call at least 3 functions
def twenty_twenty_over():
    if final > 0:
        print(final, "days until this dumpster fire of a year is over!")
    elif final == 0:
        print ("Happy New Year!")
    elif final < 0:
        print ("2021 here we come! \n")
#FEATURE Create Loop 
def main_menu():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Commute Main Menu")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Please select an option below.")
    print("1.Calculate Commute")
    #option to call function user_info
    print("2. Countdown to 2021 Clock!")
    print("Enter 0 to Exit the Program")
    choice = input("\n Enter 1, 2, or 0 please! ").lower()
    if choice == "1":
        Commute.user_info()
    elif choice =="2":
        print("Work in Progress! Check out my datetime!. \n")
        twenty_twenty_over()
        main_menu()                 
    elif choice == "0":
        print("\n Thanks for checking out my Python code! Hopefully I passed? \n")
        quit()

  
class Commute:

# function used to determine and display if user input is lower or higher than the US average
    def user_info():
        user_commute_time = input("What is your current one-way commute time in minutes?")
        user_city = input("What city do you live in?")
#FEATURE Build a conversion tool that converts user input to another type and displays it (minutes to days)
        commute_time = float(user_commute_time)
        commute_diff = NATIONAL_AVERAGE - commute_time
        commute_time_minutes = commute_time
        #Calculating round trip daily
        round_trip_min = commute_time_minutes * 2
        #Converting minutes to hours
        hours_per_day = round(round_trip_min / 60)
        #Converting hours to days
        hours_per_year = round(hours_per_day * 5 * 52)
        days_per_year = round(hours_per_year / 24)
            #Converting commute input into a integer
        if commute_time > NATIONAL_AVERAGE:
            print (' Your one-way commute is {} minutes HIGHER than the national average. That is converted to almost {} hour(s) a day round trip, or {} days per year!  See you back in {}.'.format(commute_diff, hours_per_day, days_per_year, user_city))
        
        elif commute_time < NATIONAL_AVERAGE:
            print ('Your one-way commute is {} minutes LOWER than the national average. That is converted to almost {} hour(s) a day round trip, or {} days per year!  See you back in {}.'.format(commute_diff, hours_per_day, days_per_year, user_city))
            
        else:
            print ('Your one-way commute is the SAME as the national average! See you back in {}.'.format(user_city))

main_menu()
