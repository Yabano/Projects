
# creating a new dictionary
my_dict ={"java":100, "python":112, "c":11}
 
# list out keys and values separately
key_list = list(my_dict.keys())
val_list = list(my_dict.values())
 
# print key with val 100
position = val_list.index(100)
print(val_list[position])