# https://leetcode.com/problems/two-sum/

# 1. Two Sum
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# Example 2:
# Input: nums = [3,2,4], target = 6
# Output: [1,2]

# Example 3:
# Input: nums = [3,3], target = 6
# Output: [0,1]

# My solution 1 - not correct
def two_sum(nums, target):

    new_list = []

    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if nums[i] + nums[j] == target:
                # print(nums[i], nums[j])
                new_list.extend([i,j])
    
    return new_list

# print(two_sum([3,2,4], 6))


# My solution 2
def two_sum(nums, target):

    new_dict = {}
        
    for i in range(len(nums)):
        if nums[i] not in new_dict:
            new_dict[nums[i]] = [i]
        else:
            new_dict[nums[i]] += [i]
    # print(new_dict) #{3: [0], 2: [1], 4: [2]}
    
    for j in range(len(nums)):
        a = nums[j]
        b = target - nums[j]
        print(a)
        print(b)
        if b in new_dict:
            array = new_dict[b]
            for x in array:
                if x != j:
                    return [j, x]

print(two_sum([3,2,4], 6))


# My solution 3
def two_sum(nums, target):

    new_dict = {}

    for i, num in enumerate(nums):
        j = target - num
        if j in new_dict:
            return new_dict[j], i #1,2
        else:
            new_dict[num] = i

# print(two_sum([3,2,4], 6))