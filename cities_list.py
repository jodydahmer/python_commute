#cities_list.py
#Practicing lists in Python, specifically nesting lists

#Format = City, State,  Region , Commute Time in minutes
national_average = 30
commute = input("What is your commute time?")
commute_time = int(commute)

city_commute = [
    ["Chicago","Illinois","Midwest","40"],    
    ["Atlanta","Georgia","South","30"],
    ["New York","New York","Northeast","45"],
    ["San Francisco", "California","West Coast","50"],

]

commute_diff = national_average - commute_time

def more_or_less() :
    if commute_diff >= 0 :
        print("more")
    else:
        print("less")

print(city_commute[0][3])
print("Here are some cities and their average commute times: ")
week_number = 1
for city in city_commute: 
    print("* If you lived in {}, you would have a {} minute commute! That means you are {} minutes {} than the national average." .format(city_commute[0][0],city_commute[0][3],commute_diff,more_or_less))


def print_cities(**kwargs)
    for key,value in kwargs.items():
        print(f'(key): {value}')

    print_teacher(name = 'Chicago' , region = 'Midwest' , commute_time = '20')