#!/bin/python3

new_line = "\n"
line = "------------------------"
print("LISTS")
print(line)

my_list = list()
my_other_list = []

print(len(my_list))


my_list = [12 , 24 ,17 , 42, 51]
my_other_list = [21, 1.78, "Alan", "López"]

print(type(my_list[1]))
print(type(my_list))

print(new_line)

## METHODS
print("METHODS")
print(line)

my_other_list.append("p4ra1lax") # add at the end of the line
print(my_other_list)


my_other_list.insert(1, "Azul")
print(my_other_list)

my_other_list.remove("Azul") # remove the first specific item
# del my_other_list[1]  #delete items by index
print(my_other_list)

my_list.pop() # remove the last item
print(my_list)
my_list.append(32)
print(my_list.pop())

my_list.sort() # sort the list
print(my_list)