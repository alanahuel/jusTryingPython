#!/bin/python3

new_line = "\n"
line = "-------------------"

# Strings

my_string = "My String"
my_other_string = "My Other String"

print(my_string + " " + my_other_string)


# Special characters

tab_string = "\t" # make a tab
new_line # make a new line


# Format 
print(new_line)
print("Format")
print(line)

name, surname, age = "Alan", "López", 21
print("My name is {} {} and my age {} years old".format(name,surname, age))
print(f"My name is {name} {surname} and my age {age} years old")
print("My name is  %s %s and my age %d years old"%(name,surname, age))

# Division

print(new_line)
print("Division")
print(line)

language = "Python"
language_slice = language[1:3]
print(language_slice)

language_slice_2 = language[-2]
print(language_slice_2)

# Reverse

reversed_language = language[::-1]
print(reversed_language)

#Functions
print(new_line)
print("Function")
print(line)

print(language.capitalize())
print(language.upper())
print(language.count("t"))
print(language.isnumeric())
print(language.lower())
print(language.upper().isupper())
print(language.startswith("py"))
