# Given a string, return the same string, reversed.

# For example, as “porcupine” would reverse to “enipucrop”:
# >>> rev_string("porcupine")
# 'enipucrop'


# Start my solution:

# My solution 1
def rev_string(astring):

    # astring[0] = astring[-1]
    # print(astring) #str no item assignment

    # return astring[::-1] #enipucrop

    new_astring = ""

    for i in range(len(astring), 0, -1):
        new_astring += astring[i-1]
    
    return new_astring

print(rev_string("porcupine"))

