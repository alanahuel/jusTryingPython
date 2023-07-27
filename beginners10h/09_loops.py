#!/bin/python3

def new_line():
    print("\n")
def line():
    print("--------------------------------")
    
print("LOOPS")
line()

# WHILE

print("WHILE")
line()

my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition +=1
else:  # Optional 
    print("My condition is grater than 10") 
line()

# FOR

print("FOR")
line()

my_list = [12 , 24 ,17 , 42, 51]

for x in my_list:
    print(x)

