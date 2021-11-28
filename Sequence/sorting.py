pangram = 'the quick brown fox jumps over the lazy dog'

letters = sorted(pangram)
print(letters)

numbers = [2.3, 4.5, 3.1, 9.2, 1.6]
sorting = sorted(numbers)
print(id(sorting))
print(sorting)

numbers.sort()
print(id(numbers))
print(numbers)