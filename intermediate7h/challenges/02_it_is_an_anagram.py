## CHALLENGE 2 ##

'''
 Write a function that receives two words (String) and returns
 true or false (Bool) depending on whether they are anagrams or not.
 - An Anagram consists of forming a word by rearranging ALL
   the letters of another initial word.
 - It is NOT necessary to check whether both words exist.
 - Two words that are exactly the same are not anagrams.
 ''' 

def is_anagram(word_one, word_two):
    if word_one.lower() == word_two.lower():
        return False
    return sorted(word_one.lower()) == sorted(word_two.lower())
    
print(is_anagram(input("First word: "), input("Second word: ")))    
    