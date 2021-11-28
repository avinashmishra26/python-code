list_shoppping = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

#exclude spam
for item in list_shoppping :
    if item != "spam" :
        print("Buy "+item)

print()

#exclude spam using continue
for item in list_shoppping :
    if item == "spam" :
        continue
    print("Buy "+item)


print()
#use break
for item in list_shoppping :
    if item == "spam" :
        print("Spam found "+item)
        break
