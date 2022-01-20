# Given a string, return the same string, reversed.

# For example, as “porcupine” would reverse to “enipucrop”:
# >>> rev_string("porcupine")
# 'enipucrop'


# Start my solution:

# My solution 1 - without using python built-in functions reverse or reversed
def rev_string(astring):

    # astring[0] = astring[-1]
    # print(astring) #str no item assignment

    # return astring[::-1] #enipucrop

    new_astring = ""

    for i in range(len(astring), 0, -1):
        new_astring += astring[i-1]
    
    return new_astring

print(rev_string("porcupine"))


# My solution 2 - without using python built-in functions reverse or reversed
def rev_string(astring):

    new_string = list(astring) # string to list
    # print(new_string) #['p', 'o', 'r', 'c', 'u', 'p', 'i', 'n', 'e']

    for i in range(len(new_string) // 2):
        # x, y = y, x
        new_string[i], new_string[-i-1] = new_string[-i-1],new_string[i]

    # print(new_string) #['e', 'n', 'i', 'p', 'u', 'c', 'r', 'o', 'p']
    return "".join(new_string) # list to string

print(rev_string("porcupine"))
