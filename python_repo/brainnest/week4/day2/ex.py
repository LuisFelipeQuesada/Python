#how to write a code using list comprehension to receive a lists of lists and returns and flat list?
list_c = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
def flatten_list(list):
    return [i for sublist in list for i in sublist]
print(flatten_list(list_c))

#Use a list comprehension to extract specific elements from a list of dictionaries.
def extract_elements(dict_list, key):
    return [i[key] for i in dict_list]

dicts = [{ "name": "Tom", "age": 10, "city": "Madrid" },
         { "name": "Mark", "age": 5, "city": "London" },
         { "name": "Pam", "age": 7, "city": "Paris" },
         { "name": "Jane", "age": 12, "city": "Berlin" }]
print(extract_elements(dicts, "city"))

