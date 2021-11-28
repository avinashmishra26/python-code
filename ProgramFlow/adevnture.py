available_exists = ["north", "south", "east", "west"]

print(type(available_exists))

chosen_exit = ""

for i in available_exists:
    print(available_exists.index(i))

print()

while chosen_exit not in available_exists :
    chosen_exit = input("please choose a direction: ")
    if chosen_exit.casefold() == "quit" :
        print("game over")
        break

print("you are good to leave")