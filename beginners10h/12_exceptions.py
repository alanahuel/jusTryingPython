#!/bin/python3

# EXCEPTION HANDLING

def new_line():
    print("\n")
def line():
    print("--------------------------------")
    
print("EXCEPTION HANDLING")

numberOne = 5
numberTwo = 3
numberTwo = "3"

# Try Except  
line()
try:
    print(numberOne + numberTwo)
except:
    print("Has ocurred an Error!")
    
# Try Except Else
line()
numberTwo = int(numberTwo)

try:
    print(numberOne + numberTwo)
except:
    print("Has ocurred an Error!")
else:
    print("There were not problems")
    
# Try Except Else Finally
line()
try:
    print(numberOne + numberTwo)
except:
    print("Has ocurred an Error!")
else:
    print("There were not problems")
finally:
    print("The program is running")
    
    
# Exceptions of Types
line()
try:
    print(numberOne + numberTwo)
except ValueError:
    print("Has ocurred an ValueError!")
except TypeError:
    print("Has ocurred an TypeError!")
    
# Exception Capture Information
line()
try:
    print(numberOne + str(numberTwo))
except TypeError as error:
    print("Has ocurred an TypeError!")
    print(error)