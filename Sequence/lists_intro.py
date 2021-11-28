computer_parts = ["computer",
                  "monitors",
                  "keyboard",
                  "mouse",
                  "mouse mat"]


for index in range(len(computer_parts)) :
    if "mouse" == computer_parts[index] :
        print(index)


print(computer_parts[0:3])
print(computer_parts[-1])

print()

print(computer_parts[-1::-1])

print(id(computer_parts))

computer_parts.append("Laptop")
print(computer_parts)
print(id(computer_parts))

computer_parts[3]= "tracball"
print(computer_parts)


