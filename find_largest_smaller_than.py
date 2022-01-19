# Given an ordered list of numbers and a number, return the index of the largest number in the list that is smaller than that number.

# For example:
# >>> find_largest_smaller_than([-5, -2, 8, 12, 32], 10)
# 2

# >>> find_largest_smaller_than([-5, -2, 8, 12, 32], 33)
# 4

# >>> find_largest_smaller_than([-5, -2, 8, 12, 32], -1)
# 1

# Never find xnumber — it’s not smaller than itself!
# >>> find_largest_smaller_than([-5, -2, 8, 12, 32], 8)
# 1

# If no such number exists, return None:
# >>> find_largest_smaller_than([-5, -2, 8, 12, 32], -10) is None
# True


# Start my solution:

# My solution 
def find_largest_smaller_than(nums, xnumber):

    new_list = []

    if nums[0] > xnumber:
        return None
    
    if nums[-1] < xnumber:
        return len(nums) - 1
        
    for i in range(len(nums)):
        if nums[i] == xnumber:
            return i
        elif nums[i] < xnumber:
            new_list.append(nums[i])

    return len(new_list) - 1

print(find_largest_smaller_than([-5, -2, 8, 12, 32], 10))

