# 1. Write a lambda function that takes a list of numbers, and returns a new list containing only the positive numbers from the original list.
l = [-9,4,-34,6,1,-4,10]
result = list(filter(lambda x : (x >= 0), l))
print(result)

# 2. Write a lambda function that takes a list of dictionaries and returns a new list of dictionaries sorted by a specified key.

dict_l = [
    {'name': 'Alice', 'age': 55, 'city':'London'},
    {'name': 'Bob', 'age': 25, 'city':'Berlin'},
    {'name': 'Charlie', 'age': 35, 'city':'Amsterdam'},
    {'name': 'David', 'age': 40, 'city':'Paris'},
]
sort_by = 'city'
sorted_dicts = sorted(dict_l, key=lambda x: x[sort_by])
print(sorted_dicts)

# 3. Write a lambda function that takes a string and returns a new string with the first letter of each word capitalized.
word = "house"
new_s = ''.join(map(lambda x: x[0].capitalize() + x[1::], word.split()))
print(new_s)

# 4. Write a lambda function that takes a list of dictionaries and returns a new list of dictionaries that contain only the key-value pairs for which the value is greater than a specified threshold.4




