final_python.py 

#This application will take user input for their average one way commute time , compare it to a list of commute times for other cities , then use functions to determine if the user inputted commute time was larger or smaller than the US average. 

import math
from datetime import datetime


#Taking user input, want to raise ValueError in case of non number

user_commute_time = input("What is your current one-way commute time?")

#Converting input into a integer
commute_time = int(user_commute_time)


#Requirement2  datetime is used to get current date and determine what the current year is, current month is to make calculations based on the timedelta
current_date = datetime.now().date()
current_year = current_date.year
current_month = current_date.month
last_year = current_year - 1
last_two_year = last_year - 1

# Requirement 1 Create and use at least 3 fuctions with at least 1 returning a value used later - 4 functions are listed below
# returns a value of higher, lower, or equal to the national average commute time. 

# function to print end commute result (DRY)
def printcommute():
     print('Your total commute time is {} {} every month'.format(commute_time, ))




# function used to determine and display if user input is lower or higher than the US average
def judge_stock(): 
    try:
    
    
    if commute_time < national_average:
        print (' Your commute is HIGHER than the national average')
        printcommute()
    elif commute_time > national_average:
        print ('Your commute is LOWER than the national average')
        printcommute()
    else:
        print ('Your commute is the SAME as the national average')
        printcommute()




while True:    
    commute_time = input ('Enter your commute time or type exit to exit the program' ) 
    if ticker == "exit":
        break
    try:
        print(message)
    except ValueError:
        print("Numbers only! Please try again!")
    else:
        calc_commute()