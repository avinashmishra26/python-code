even = [2, 4, 6, 8,2]
odd = [1, 3, 5, 7, 9]

print(even.count(2))



print(min(even))
print(min(odd))

print(max(even))
print(max(odd))

print()
print(len(even))
print(len(odd))


del even[:2]
print(even)

print()
print("mississippi".count("ss"))

even.extend(odd)
print(f"extend {even}")

print(id(even))
even.sort()
print(even)
print(id(even))

even.sort(reverse=True)
print(even)


#list concatenate
number = even + odd
print(f"number {number}")

sort_numbers = sorted(number)