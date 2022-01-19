# Given list of ints, return True if any two nums in list sum to 0.

# Examples
# >>> add_to_zero([])
# False

# >>> add_to_zero([1])
# False

# >>> add_to_zero([1, 2, 3])
# False

# >>> add_to_zero([1, 2, 3, -2])
# True

# Given the wording of our problem, a zero in the list will always make this true, since “any two numbers” could include that same zero for both numbers, and they sum to zero:

# Examples
# >>> add_to_zero([0, 1, 2])
# True


# Start my solution:

# Option 1
def add_to_zero(nums):
    """Given list of ints, return True if any two nums sum to 0."""

    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if nums[i] + nums[j] == 0 or 0 in nums:
                return True
    else:
        return False

print(add_to_zero([1, 2, 3, -2]))


# Option 2
def add_to_zero(nums):
    
    new_nums = set(nums)

    for num in new_nums:
        if -num in new_nums:
            return True
        # else:
        #     return False

    return False

print(add_to_zero([1, 2, 3, -2]))


# Option 2
def add_to_zero(nums):

    new_nums = set(nums)

    return any(-num in new_nums for num in nums)

print(add_to_zero([1, 2, 3, -2]))





