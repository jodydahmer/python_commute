Hours_Day = 1

Hours_remaining = 24 

#Output how many hours are remaining in a day for a commute scheduling app

print("There are {} hours remaining in your day".format(Hours_remaining))

#Gather user commute time and assign it to a new variable

commute_time = input("What is your personal daily commute time?")

#Prompt user by name and ask how many hours they drive
user_commute_time = input("How long is your daily round-trip commute, {}?" .format(commute_time))
try:    
    user_commute_time = int(user_commute_time)
    if user_commute_time > Hours_remaining:
        raise ValueError("There are only {} hours in a day!".format(Hours_remaining))
        except ValueError:
        print("Oh no, we need to be able to use a number!")
    else:

        #Calculate total time spent in day commuting by converting commute time into hours
        daily_commute = user_commute_time / 60
        print("Your daily commute time is {} days".format(daily_commute))
        #Output the price to the screen 


        #Ask user if they want to proceed
should_proceed = input("Do you want to proceed? y/n")
        
    if should_proceed.lower() == "y" : 

            #Print out to the screen difference in hours when days total is displayed
                print("You have {} hours remaining in your day once we subtract your commute!".format(Hours_remaining))
            #And then decrement the commute time total from  total hours remaining in day 

Hours_remaining -= daily_commute
