# Lists
# Tuples
# Sets
python_set_type = {"Wroclaw", "Warszawa", "Bialystok"}  # Only unique elements. No indexing
python_set_type.add("Lodz")
print(python_set_type)

# Dicts
python_dict_type = {1:"Piotr", 2:"Adam", 3:"Pawel"}
print(python_dict_type.get(1))
print(python_dict_type[2])
python_dict_type[4]="Ola"

for key in python_dict_type.keys():
    print(key)

for value in python_dict_type.values():
    print(value)

del python_dict_type[1]
