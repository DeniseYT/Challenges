# In this challenge, you’ll write a function that is given a list of items and returns a new list of those items, 
# in the same order, but with duplicate removed.

# For example:
# >>> deduped([1, 1, 1])
# [1]

# Keep items in the order where they first appeared:
# >>> deduped([1, 2, 1, 1, 3])
# [1, 2, 3]

# A list with no duplicates would return the same:
# >>> deduped([1, 2, 3])
# [1, 2, 3]

# This should return a new list, not mutate the existing list:
# >>> a = [1, 2, 3]
# >>> b = deduped(a)
# >>> a == b
# True
# >>> a is b
# False

# An empty list should return an empty list:
# >>> deduped([])
# []


# Start my solution:

# My solution 1
# set do not maintain order
def deduped(items):

    new_list = []
    set_items = set(items)
    # print(set_items) #{1,2,3} or #{1,3,2}

    new_list += set_items
    return new_list

print(deduped([1, 3, 1, 1, 2]))


# My solution 2
# O(n**2) runtime
def deduped(items):

    new_list = []

    for item in items:
        if item not in new_list:
            new_list.append(item)
    
    return new_list

print(deduped([1, 3, 1, 1, 2]))


# My solution 3
# use set to keep track of what we seen, then use a list to hold the results.
def deduped(items):

    seen = set() #keep track of items we've seen
    new_list = [] #hold our results

    for item in items:
        if item not in seen:
            new_list.append(item)
            seen.add(item)
    # print(new_list)
    # print(seen) #{1,2,3}
    
    return new_list

print(deduped([1, 3, 1, 1, 2]))
