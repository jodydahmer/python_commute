request = input("What would you like?  ")
while "please" not in request:
    request = input("You seem to be missing a magic word.  What would you like?  ")
print("Here you go!")