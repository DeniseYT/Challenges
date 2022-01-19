# Given an integer n, return a list containing n unique random numbers between 1-10, inclusive. (That is, do not repeat any numbers in the returned list.)

# You can trust that this function will never be called with n < 0 or n > 10.

# For example:
# >>> lucky_numbers(2)
# [3, 7]

# It’s legal to ask for no numbers:
# >>> lucky_numbers(0)
# []

# And if we ask for all numbers, we shouldn’t get any repeats:
# >>> sorted(lucky_numbers(10))
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# Start my solution:

import random
def lucky_numbers(n):

    nums = list(range(1,11))
    lucky_nums = []

    for i in range(n):
        num = random.choice(nums)
        # print(num) #9, 8
        nums.remove(num) 
        # print(nums) #[1, 2, 3, 4, 5, 6, 7, 10]
        lucky_nums.append(num)
    
    return lucky_nums

print(lucky_numbers(2))

