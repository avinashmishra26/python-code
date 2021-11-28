list_shoppping = ["milk", "pasta", "eggs", "spam", "bread", "rice"]


item_to_find = "spam"
found_at = None

found_at_list = None

for index in range(len(list_shoppping)) :
    if list_shoppping[index] == item_to_find :
        found_at = index
        break

if found_at is not None:
    print("Item found at position {}".format(found_at))
else :
    print("{} not found".format(item_to_find))

#One more way

for item_to_find in list_shoppping :
    found_at_list = list_shoppping.index(item_to_find)