## CHALLENGE 5 ##

'''
 * Write a program that checks whether a number is prime or not.
 * Once this is done, print the prime numbers between 1 and 100.
'''

def is_prime():
    for number in range(1, 101):
        
        if number >= 2:
            
            is_divisible = False
            
            for i in range(2,number):
                
                if number % i == 0:
                    is_divisible = True
                    break
                
            if not is_divisible:
                print(number)
    print(number)        
is_prime()
    