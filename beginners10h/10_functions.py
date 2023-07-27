#!/bin/python3

def new_line():
    print("\n")
def line():
    print("--------------------------------")
    

def sum_two_values(first_number, second_number):
    print(first_number + second_number)
    
sum_two_values(3, 7)

def sum_two_values_with_return(first_number, second_number):
    return first_number + second_number

result = sum_two_values_with_return(10, 5)

print(result)

def print_name(name, surname):
    print(f"{name} {surname}")

print_name("Alan", "López")


def print_name_with_default(name, surname, aka = "Without aka"):
    print(f"{name} {surname} {aka}")

print_name_with_default("Alan", "Lopez")
    
def print_texts(*text): # Use the '*' for unlimited parameters 
    print(text)