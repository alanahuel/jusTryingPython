## CHALLENGE 3 ##

'''
- Write a program that prints the first 50 numbers of the Fibonacci sequence starting at 0.
- The Fibonacci series is composed of a sequence of numbers where the next number is always 
  the sum of the two previous ones.
   
   [*] 0, 1, 1, 2, 3, 5, 8, 13...
'''

def fibonacci():
    
    prev = 0
    next = 1
    
    for i in  range (0,50):
        print(prev)
        
        fib = prev + next
        prev = next
        next = fib
        
fibonacci()