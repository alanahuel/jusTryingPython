#!/bin/python3

def new_line():
    print("\n")
def line():
    print("------------------------------------")
    
print("TUPLES")
line()

my_tuple = (35, 1.77, "Alan", "López")
my_other_tuple = (21, 42, 37, 42)
print(my_tuple)
print(my_other_tuple)
print(type(my_tuple))


print(my_tuple[0])
print(my_tuple[-1])

print(my_tuple.count("Alan")) # count the coincidences
print(my_tuple.index("Alan")) 

# ERROR : 'tuple' object does not support item assignment 
# my_tuple[1] = 1.80
# print(my_tuple)
    
my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)
print(my_sum_tuple[3:6])

# del my_tuple
# print(my_tuple) NameError: name 'my_tuple' is not defined