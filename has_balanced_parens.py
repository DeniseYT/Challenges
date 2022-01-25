# Given a string, return True or False depending on whether that string has balanced parentheses.

# For the purposes of this problem, you only need to worry about parentheses (( and )), 
# not other opening-and-closing marks, like curly brackets, square brackets, 
# or angle brackets.

# For example:
#  >>> has_balanced_parens("()")
#  True
#  >>> has_balanced_parens("(Oh Noes!)(")
#  False
#  >>> has_balanced_parens("((There's a bonus open paren here.)")
#  False
#  >>> has_balanced_parens(")")
#  False
#  >>> has_balanced_parens("(")
#  False
#  >>> has_balanced_parens("(This has (too many closes.) ) )")
#  False

# You may consider a string with no parentheses balanced:
# >>> has_balanced_parens("Hey...there are no parens here!")
# True


# My Solution
def has_balanced_parens(phrase):
    """Does a string have balanced parentheses?"""

    left = []
    right = []

    for item in phrase:
        if item == "(":
            left.append(item)
        if item == ")":
            right.append(item)
    
    # print(left)
    # print(right)

    if len(left) == len(right):
        return True
    
    return False

print(has_balanced_parens("Hey...there are no parens here!"))