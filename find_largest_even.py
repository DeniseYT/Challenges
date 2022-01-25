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
    print(new_lst) #['what', 'I', 'love', 'is', 'technical', 'challenge']

    new_dict = {} 
    even_lst = []

    for word in new_lst:
        if len(word) not in new_dict:
            new_dict[word] = len(word) #{'what': 4, 'I': 1, 'love': 4, 'is': 2, 'technical': 9, 'challenge': 9}
    
    for word, value in new_dict.items():
        if value % 2 == 0:
            even_lst.append(word)
    
    # print(even_lst) #['what', 'love', 'is']

    largest = even_lst[0]
    # print(largest) #what

    for word in even_lst:
        if len(word) > len(largest):
            largest = len(word)
    
    return largest

print(find_largest_even("what I love is technical challenge"))




