# You will be given a list of integers, some even and some odd:
# >>> lst = [1, 2, 3, 4, 6, 8]

# Write a function that returns the indices (0-based, as usual in Python) of all the numbers which are even.
# So, for our list above, that would be:
# >>> show_evens(lst)
# [1, 3, 4, 5]


# Start my solution:

# My solution 1
def show_evens(nums):

    new_list = []

    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_list.append(i)
    
    return new_list

print(show_evens([1, 2, 3, 4, 6, 8]))


# My solution 2 - use enumerate method
def show_evens(nums):

    new_list = []

    for i, num in enumerate(nums):
        if num % 2 == 0:
            new_list.append(i)
    
    return new_list
            
print(show_evens([1, 2, 3, 4, 6, 8]))