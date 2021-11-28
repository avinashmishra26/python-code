# for i in range(1, 13):
#     print("No. {0:2} squared is {1:3} and cubed is {2:4}".format(i, i ** 2, i ** 3))
#     #print(f"No. {i:2} squared is {i ** 2:3} and cubed is {i ** 3:4}".format(i, i ** 2, i ** 3))
#     print("*" * 80 )

name = input("Please enter your name  ")
age = int(input(f"What's your age? {name} "))

# if age >=18:
#     print("You can vote")
#     print("Please put an X in the box")
# else:
#     print("Please come back in {} years".format(18-age))


if age < 18:
    print("Please come back in {} years".format(18-age))
elif age == 900:
    print("Sorry, Yoda, you die in return of the Jedi")
else:
    print("You can vote")
    print("Please put an X in the box")