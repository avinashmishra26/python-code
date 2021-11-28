result = True

another_result = result

print("result {}",format(id(result)))
print("another_result {}".format(id(another_result)))

result = False
print("result {}",format(id(result)))
print("another_result {}".format(id(another_result)))


str_result = "Correct"
another_str_result = str_result

print(id(str_result))
str_result += 'ish'

print(id(str_result))
print(id(another_str_result))