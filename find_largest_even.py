# Atlassin
# find the largest even number

# input = [2,2,1,8,3,5]
# output = 8


def find_largest_even(lst):
    """Find largest even number in a list"""

    new_lst = []

    for num in lst:
        if num % 2 == 0:
            new_lst.append(num)
    
    return max(new_lst)

print(find_largest_even([2,2,1,8,3,5]))




