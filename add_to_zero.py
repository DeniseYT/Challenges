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


def add_to_zero(nums):
    """Given list of ints, return True if any two nums sum to 0."""

    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if nums[i] + nums[j] == 0 or 0 in nums:
                return True
    else:
        return False

print(add_to_zero([1, 2, 3, -2]))
