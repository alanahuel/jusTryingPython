#!/bin/python3

# Varibles

my_string_variable = 'My String Variable'
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

print(my_string_variable, my_int_variable, '!')

# Transform data type
my_str_int_variable = str(my_int_variable)
print(type(my_str_int_variable))


# System variables

print(len(my_string_variable)) # counts every character, also the blanc spaces

# Variables in just one line. WARNING!! This's not a good practice

name, surname, alias, age = "Alan", "López", "p4ra1lax", 21
print("My name:", name, surname, ". My age:", age, ". And mya aka is:", alias)

# Inputs

name = input("What's your name?")
age = input("How old are you?")

print("Then, your name is " + name + " and you are " + age + " years old")