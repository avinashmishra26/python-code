letters ="abcdefghijklmnopqrstuvwxyz"

print(letters[2:5:1])

backwards = letters[25::-1]
print(backwards)

#same as above
print(letters[::-1])


#print qpo
print("test "+letters[-10:-13:-1])
#same as above
print(letters[16:13:-1])

#print edbca
print(letters[-22::-1])

#print last 8 character
print(letters[:-9:-1])

#last 4 value
print(letters[-4:])

#last character
print(letters[-1:])

#first character
print("letters[-26::-1] "+letters[-26::-1])
#same as above
print(letters[:1])
#same as above
print(letters[0])

emptyLetter = ""
#print(emptyLetter[0])  #error
