# Compute the sum of a list of numbers.

# For example:
# >>> sum_list([5, 3, 6, 2, 1])
# 17


# Start my solution:

# My solution 
def sum_list(num_list):

    total = 0

    for num in num_list:
        total += num
    
    return total

print(sum_list([5, 3, 6, 2, 1]))