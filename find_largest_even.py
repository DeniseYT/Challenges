# Atlassin
# find the largest even number word

# input = "what I love is technical challenge"
# output = [what]

# explanation
# input_lenth = [4,1,4,2,9,9]
# return the first word of even number

# Solution 1 - Wrong
def find_largest_even(lst):
    """Find largest even number in a list"""

    new_lst = lst.split() 
    # print(new_lst) #['what', 'I', 'love', 'is', 'technical', 'challenge']

    largest_length = 0

    for word in new_lst:
        if len(word) > largest_length:
            largest_length = len(word)
    
    return word

print(find_largest_even("what I love is technical challenge"))


# Solution 2 - Correct
def find_largest_even(lst):

    new_lst = lst.split() #['what', 'I', 'love', 'is', 'technical', 'challenge']
    new_even_lst = []

    for word in new_lst:
        if len(word) % 2 == 0:
            new_even_lst.append(word)
    
    return new_even_lst[0]

print(find_largest_even("what I love is technical challenge"))


