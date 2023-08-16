## FILE HANDLING ##

import os

print(os.getcwd())

# .txt file
with open('intermediate7h/my_file.txt', 'w+') as txt_file: 
    txt_file.write("My name is Alan\nMi surname is Lopez\n21 years old\nMy favorite programming language is Python")
    txt_file.seek(0)  # Move the pointer back to the beginning of the file
    for line in txt_file.readlines():
        print(line)

    txt_file.write("\nThough also love Go")
    txt_file.seek(0)  # Move the pointer back to the beginning of the file
    for line in txt_file.readlines():
        print(line)
