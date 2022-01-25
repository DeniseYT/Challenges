# Atlassin
# find the largest even number word

# input = "what I love is technical challenge"
# output = [what]

# explanation
# input_lenth = [4,1,4,2,9,9]
# return the first word of even number


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




