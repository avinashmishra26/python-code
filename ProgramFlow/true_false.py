day = "Saturday"
temperature = 40
raining = False

if day == "Saturday" and temperature > 27 and not raining :
    print("Go swimming")
else :
    print("Learn python")


#Other truth values

if 0:
    print("True")
else:
    print("False")

name = input("Your Name ")

if name :
    print("Hello {}".format(name))
else:
    print("Are you with no name")