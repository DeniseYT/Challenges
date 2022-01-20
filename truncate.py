# Write a function that takes in a string and returns a string where any repeating characters have been truncated to one character. For example:

# >>> truncate('aaaaabbbbbcccaaaa')
# 'abca'

# >>> truncate('hi there')
# 'hi there'

# >>> truncate('hi   !!! wooow')
# 'hi ! wow'


# Start my solution:

# My solution 
def truncate(astring):

    new_string = []

    for letter in astring:
        if letter not in new_string or letter != new_string[-1]:
            new_string.append(letter)
    
    # print(new_string) #['h', 'i', ' ', '!', ' ', 'w', 'o', 'w']
    return "".join(new_string) #convert list to string

print(truncate('hi   !!! wooow'))