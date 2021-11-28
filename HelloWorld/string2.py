parrot = "Norwegian Blue"

print(parrot)

print(parrot[3])

print(parrot[4])

print(parrot[9])

print(parrot[3])
print(parrot[6])
print(parrot[8])


print(parrot[9])

print(parrot[-1])
print(parrot[-14])


#slicing upto but not including
print()
print(parrot[0:6])

print(parrot[0:14])

print(parrot[0:-1])

print(parrot[3:5])

print(parrot[0:9])
#same as above
print(parrot[:9])

print(parrot[:-2])

print(parrot[-4:-2])
#same as above
print(parrot[-4:12])

print(parrot[10:])
#same as above
print(parrot[10:14])


print()
#full string
print(parrot[:6] + parrot[6:])
print(parrot[:])


#STEP
print('******** STEP *****')
print(parrot[0:6])
print(parrot[0:6:1])
print(parrot[0:6:2])
print(parrot[0:6:3])

print(parrot[1 ::2])

number = "9,223;372:036 854,775;807"
separarors = number[1::4]

values = "".join(char if char not in separarors else " " for char in number).split()

print(values)


