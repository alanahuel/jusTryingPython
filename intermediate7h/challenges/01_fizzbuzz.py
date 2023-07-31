
## CHALLENGE 1 ## 

"""
 Write a program that prints to the console (using a print statement) the
 numbers from 1 to 100 (both included) with a newline between each print,
 replacing the following:
  - Multiples of 3 with the word "fizz".
  - Multiples of 5 with the word "buzz".
  - Multiples of 3 and 5 with the word "fizzbuzz".
"""

def fizzbuzz():
  for i in range(1, 101):
    if (i % 3 == 0 and i % 5 == 0):
      print("FizzBuzz")
    elif (i % 3 == 0):
      print("Fizz")
    elif (i % 5 == 0):
      print("Buzz")
    else: 
      print(str(i))

fizzbuzz()