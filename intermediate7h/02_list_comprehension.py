## LIST COMPREHENSION ## 

def line():
    print("--------------------------------")
    


my_original_list = [1, 2 ,3, 4, 5, 6, 7]
print(my_original_list)

my_list  = [i * 2 for i in range(9)]
print(my_list)
line()

def sum_five(number):
    return number + 5

my_list  = [sum_five(i) for i in range(9)]
print(my_list)
line()


