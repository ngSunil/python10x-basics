# Dictionary
dict = {'key1': 1, 'key2': 'test', 'key3': [1,33], 'key4': (2,3)}
print(dict['key3'])
my_dict = {1:'a', 2:'b', 3:'c'}
my_dict['animal'] = 'elephant'
del(my_dict[1])
print(my_dict)
# find whether key is present in a dictionary
print('key1x' in dict)
# get all keys/ values from the dictionary
print(dict.keys(), dict.values())
# using .get on dict to find a key
print(dict.get('sunil', "'Sunil' not found" ))
