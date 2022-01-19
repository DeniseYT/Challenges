# Find the largest integer in a list of integers.

# For example:
# >>> max_num([5, 3, 6, 2, 1])
# 6


# Start my solution:

# My solution 
def max_num(num_list):

    largest = num_list[0]

    for num in num_list:
        if num > largest:
            largest = num
    
    return largest

print(max_num([5, 3, 6, 2, 10]))