#Class definition practice, should revise features to average commute times of cities

class Person:

    def __init__(self, name, surname, birthdate, address, telephone, email):
        self.name = name
        self.surname = surname
        self.birthdate = birthdate

        self.neighborhood = neighborhood
        self.telephone = telephone
        self.email = email

    def age(self):
        today = datetime.date.today()
        age = today.year - self.birthdate.year

        if today < datetime.date(today.year, self.birthdate.month, self.birthdate.day):
            age -= 1

        return age

person = Person(
    "Jane",
    "Doe",
    datetime.date(1992, 3, 12), # year, month, day
    "Smoketown",
    "555 867 5309",
    "jane.doe@example.com"
)

print(person.name)
print(person.email)
print(person.age())




#I need to make sure I can use the mapping feature to use my geodata






from matplotlib import pyplot

fig, ax = pyplot.subplots()
ax.plot([commute.day for commute in commutes],
        [commute.took.total_seconds() / 60 for commute in commutes])

ax.set(xlabel='day', ylabel='commute (minutes)',
       title='Daily commute')
ax.grid()
pyplot.show()