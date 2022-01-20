# Is the word an anagram of a palindrome?

# A palindrome is a word that reads the same forward and backwards (eg, “racecar”, “tacocat”). 
# An anagram is a rescrambling of a word (eg for “racecar”, you could rescramble this as “arceace”).

# Determine if the given word is a re-scrambling of a palindrome.

# The word will only contain lowercase letters, a-z.

# For example:
# >>> is_anagram_of_palindrome("a")
# True
# >>> is_anagram_of_palindrome("ab")
# False
# >>> is_anagram_of_palindrome("aab")
# True
# >>> is_anagram_of_palindrome("arceace")
# True
# >>> is_anagram_of_palindrome("arceaceb")
# False


# Start my solution:

# My solution 
def is_anagram_of_palindrome(word):

    new_dict = {}

    for letter in word:
        if letter not in new_dict:
            new_dict[letter] = 1
        else:
            new_dict[letter] += 1
    
    # print(new_dict) #{'a': 2, 'r': 1, 'c': 2, 'e': 2, 'b': 1}
    # print(new_dict.values()) #dict_values([2, 1, 2, 2, 1])

    count = 0

    for item in new_dict.values():
        if item % 2 != 0:
            count += 1

    if count > 1:
        return False
    else:
        return True

print(is_anagram_of_palindrome("arceaceb"))