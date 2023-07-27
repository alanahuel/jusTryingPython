#!/bin/python3

def new_line():
    print("\n")
def line():
    print("--------------------------------")
    
print("CONDITIONALS")
line()

my_condition = True # False

if my_condition:
    print("Runs 'if' condition")
    
line()

my_condition = 5 * 2

if my_condition <= 10:
    print("The result <= 10")
elif my_condition == 10:
    print("The result is 10")
else:
    print("The result is not 11")