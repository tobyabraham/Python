# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


from traceback import print_stack


def find_anagram():
    # [assignment] Add your code here
    word = input("Enter first word here:")
    anagram = input("Enter second word here:")
    s1 = word.lower()
    s2 = anagram.lower()
    if len(s1) == len(s2):
        sort_s1 = sorted(s1)
        sort_s2 = sorted(s2)

        if sort_s1 == sort_s2:
            return True

        else:
            return False
    else:
        return False
        
print(find_anagram())    


