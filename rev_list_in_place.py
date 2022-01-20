# Reverse a list in-place. Remember, for this to be “in-place” it can only use a small, constant amount of extra storage space, so no duplicating the list!

# For example:
# >>> lst = [1, 2, 3]
# >>> rev_list_in_place(lst)
# >>> lst
# [3, 2, 1]


# Start my solution:

# My solution 1
def rev_list_in_place(lst):

    for i in range(len(lst) // 2):
        
        a = lst[i]
        lst[i] = lst[-i-1] 
        lst[-i-1] = a
    
    return lst
        
print(rev_list_in_place([1, 2, 3]))