# Given a list of numbers, return the smallest and the largest number.

# # Examples
# >>> find_range([3, 4, 2, 5, 10])
# (2, 10)

# >>> find_range([43, 3, 44, 20, 2, 1, 100])
# (1, 100)

# For an empty list, it should return None as both smallest and largest:
# >>> find_range([])
# (None, None)

# Make sure it works with a list of one item, which is both smallest and largest:
# >>> find_range([7])
# (7, 7)


# Start my solution:

def find_range(nums):

    smallest = min(nums)
    largest = max(nums)

    return smallest, largest

print(find_range([3, 4, 2, 5, 10]))

