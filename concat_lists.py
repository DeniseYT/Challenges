# Given two lists. concatenate them (that is, combine them into a single list).
# For example, given [1, 2] and [3, 4]:

# # Examples
# >>> concat_lists([1, 2], [3, 4])
# [1, 2, 3, 4]

# It should work if either list is empty:

# # Examples
# >>> concat_lists([], [1, 2])
# [1, 2]

# >>> concat_lists([1, 2], [])
# [1, 2]

# >>> concat_lists([], [])
# []


# Start my solution:

# Option 1
def concat_lists(list1, list2):

    new_list = []

    for item1 in list1:
        new_list.append(item1)
    
    for item2 in list2:
        new_list.append(item2)

    return new_list

print(concat_lists([], [1, 2]))


# Option 2
def concat_lists(list1, list2):

    for item in list2:
        list1.append(item)
    
    return list1

print(concat_lists([], [2,3]))

