#!/bin/python3

def new_line():
    print("\n")
def line():
    print("--------------------------------")
    
print("DICTIONARIES")
line()


my_dict = dict()
my_other_dict = {}

my_other_dict = {"Name":"Alan", "Surname":"López", "Age":21, 1:"Python"}
my_dict = {
    "Name":"Alan", 
    "Surname":"López", 
    "Age":21, 
    "Languages":{"Python", "Swift", "Kotlin"}
    }

print(my_dict)
line()

my_dict["Street"] = "P4ra1lax Street"
print(my_dict)
line()

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())