#!/bin/python3

def new_line():
    print("\n")
def line():
    print("--------------------------------")
    
    
print("CLASSES")
line()

class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
    def walk (self):
        print(f"{self.name} is walking")


my_person = Person("Alan", "López")
print(f"{my_person.surname} {my_person.name}")
my_person.walk()