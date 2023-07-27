#!/bin/python3

def new_line():
    print("\n")
def line():
    print("------------------------------------")


print("SETS")
line()

my_set = set()
my_other_set = {}  # Originally is a dictionary
print(type(my_other_set))
print(type(my_set))

my_other_set = {"Alan", "López", 21}
print(type(my_other_set))
new_line()

print(len(my_other_set))

my_other_set.add("p4ra1lax")
print(my_other_set) # Set is a messy element

my_other_set.add("p4ra1lax")
print(my_other_set) # Set doesn't admit repeated elements

print("Para1lax" in my_other_set)
print("p4ra1lax" in my_other_set) # Check if there is a coincidence 

my_other_set.remove("p4ra1lax")
print(my_other_set)

my_other_set.clear()
print(len(my_other_set))


# del my_other_set
# print(my_other_set) NameError: name 'my_tuple' is not defined

my_set = {"Alan", "López", 31}
my_list = list(my_set)
print(type(my_list))

new_line()

my_other_set = {"Python", "Bash", "Go", "C++"}

my_new_set = my_set.union(my_other_set)
print(my_new_set.union(my_new_set).union({"Rust", "Js"}))

print(my_new_set.difference(my_set))



