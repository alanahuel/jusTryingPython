## CHALLENGE 2 ##

'''
 Write a function that receives two words (String) and returns
 true or false (Bool) depending on whether they are anagrams or not.
 - An Anagram consists of forming a word by rearranging ALL
   the letters of another initial word.
 - It is NOT necessary to check whether both words exist.
 - Two words that are exactly the same are not anagrams.
 ''' 

def is_anagram(world_one, world_two):
    if world_one.lower() == world_two.lower():
        return False
    return sorted(world_one.lower()) == sorted(world_two.lower())
    
print(is_anagram("Amor", "Roma"))    
    