
import re

open("names.txt,encoding="utf-8")
#Reading a text file
open() docs
file_object.close() docs
file_object.read() docs


names_file = open("names.txt", encoding = "utf-8")
data = names_file.read()
names_file.close()

#print(data)
#print(re.match(r'Love', data))\
print(re.match(r'\w', data))

#

with open("some_file.txt") as open_file:
    data = open_file.read()