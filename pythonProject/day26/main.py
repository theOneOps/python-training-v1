import random

number = [1, 2, 3]
new_list = [n+1 for n in number]

new_range = [n*2 for n in range(1, 5) if n % 2 == 0]

print(new_range)

names = ['freddie', 'eleanor', 'dave', 'fred', 'willy', 'beth']

new_cap_names = [name.upper() for name in names if len(name) > 4]

print(new_cap_names)

dict = {new_key : random.randint(0, 100) for (new_key) in names}

print(dict)

dict_2 = {new_key+f"{len(new_key)}": new_value + len(new_key) for (new_key, new_value) in dict.items()}

print(dict_2)

dict_3 = {new_key: new_value for (new_key, new_value) in dict_2.items() if new_value > 50}

print(dict_3)