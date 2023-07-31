## CHALLENGE 5 ##

'''
 * Create a program that reverses the order of a text string
 * without using built-in language functions that do it automatically.
 * - If we input "Hello world," it would return "dlrow olleH."
'''

def reverse_string(input_string):
    reversed_string = ""
    for char in input_string:
        reversed_string = char + reversed_string
    return reversed_string

input_text = input("Introduce an string: ")
reversed_text = reverse_string(input_text)
print(reversed_text)