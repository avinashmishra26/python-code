age = int(input("How old are you? "))

#if age >= 16 and age <=65 :
if 16 <= age <=65 :
    print("Have a good day at work")

#using range
if age in range(16,66) :
    print("Have a good day at work")

if age < 16 or age > 65 :
    print("Use your free time")