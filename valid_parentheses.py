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