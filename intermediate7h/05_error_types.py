## ERROR TYPES ##

# Syntaxerror
# print "Hello Github!"
print("Hello Github!")

# NameError
language = "Spanish" # Comment for error
print(language)

# IndexError

my_list = ["Python", "Golang", "Rust", "JavaScript"]
print(my_list[-1])
print(my_list[3])
# print(my_list[4]) # Uncomment for error

# ModuleNotFoundError
# import maths # Uncomment for error
import math


# AttributeError

print(math.pi)
# print(math.PI) # Uncomment for error

# KeyError

my_dict = {"Name":"Alan", "Surname":"López", "Age":21, 1:"Python"}
print(my_dict["Age"])
# print(my_dict["surname"]) # Uncomment for error
print(my_dict["Surname"]) 



# TypeError
# print(my_list["Nombre"]) # Uncomment for error
print(my_list[0])

# ImportError

# from random import Random # Uncomment for Error
from random import random 


# ValueError

my_int = int("10")
# my_int = int("10 años") # Uncomment for error
print(type(my_int))

# ZeroDivisionError
print(4/2)
