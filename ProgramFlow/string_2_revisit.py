number = input("Please enter a series of number using any separator you like ")

separator = ""

for cha in number :
    if not cha.isnumeric():
        separator = separator + cha

print(separator)