## HIGHER ORDER FUNCTIONS ##

def sum_one(value):
    return value + 1

def sum_five(value):
    return value + 5

def sum_two_values(first_value, second_value, f_sum):
    return f_sum(first_value + second_value)

print(sum_two_values(5, 2, sum_five))


### CLOSURES ###

def sum_ten(original_value):
    def add(value):
        return value + 10 + original_value
    return add

add_closure= sum_ten(1) 
print(add_closure(5))   
print(sum_ten(5)(1))

## BUILT-IN HIGHER ORDER FUNCTIONS ##

numbers = [2, 3 , 5 , 8, 21, 43, 4, 11, 27]

#MAP

def multiply_two(number):
    return number * 2

print(list(map(multiply_two, numbers)))
print(list(map(lambda num: num * 2, numbers)))

#FILTER

def filter_greater_ten(num):
    if (num > 10):
        return True
    return False
    

print(list(filter(filter_greater_ten ,numbers)))
print(list(filter(lambda num: num > 10 ,numbers)))


