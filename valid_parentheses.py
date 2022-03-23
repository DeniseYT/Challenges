# https://leetcode.com/problems/valid-parentheses/

# 20. Valid Parentheses

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.

# Example 1:

# Input: s = "()"
# Output: true
# Example 2:

# Input: s = "()[]{}"
# Output: true
# Example 3:

# Input: s = "(]"
# Output: false


def valid_parentheses(s):

    if len(s) % 2 != 0:
        return False
    
    char = {"(" : ")", "{" : "}", "[" : "]"}
    new_char = []

    for item in s:

        if item in char:
            new_char.append(item)
    # print(new_char) # ['(', '[', '{']
    # print(new_char[-1]) # {

        elif len(new_char) != 0 and item == char.get(new_char[-1]):
            new_char.pop()

        else:
            return False
    
    return len(new_char) == 0

print(valid_parentheses("([{}])"))