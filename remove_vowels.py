# https://leetcode.com/problems/remove-vowels-from-a-string/

# 1119. Remove Vowels from a String

# Given a string s, remove the vowels 'a', 'e', 'i', 'o', and 'u' from it, and return the new string.

# Example 1:
# Input: s = "leetcodeisacommunityforcoders"
# Output: "ltcdscmmntyfrcdrs"

# Example 2:
# Input: s = "aeiou"
# Output: ""


# My solution
def remove_vowels(str):

    vowels = {"a", "e", "i", "o", "u"}
    new_str = ""

    for letter in str:
        if letter in vowels:
            letter = ""
            new_str += letter
        else:
            new_str += letter
  
    return new_str

print(remove_vowels("leetcodeisacommunityforcoders")) #"ltcdscmmntyfrcdrs"
