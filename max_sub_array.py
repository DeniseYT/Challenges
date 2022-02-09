# https://leetcode.com/problems/maximum-subarray/

# 53. Maximum Subarray

# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
# A subarray is a contiguous part of an array.

# Example 1:
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.

# Example 2:
# Input: nums = [1]
# Output: 1

# Example 3:
# Input: nums = [5,4,-1,7,8]
# Output: 23


# My solution 1
def max_sub_array(nums):

    begin_sum = 0
    total = 0

    for num in nums:
        begin_sum += num

        if begin_sum >= total:
            total = begin_sum
            # print(total) #1/4/5/6
        elif begin_sum < 0: #means negative number/sum
            begin_sum = 0 
    
    if total == 0:
        return max(nums)

print(max_sub_array([-2,1,-3,4,-1,2,1,-5,4])) #-2,-1,-4,0,-1,1,2,-3,1
# print(max_sub_array([5,4,-1,7,8])) #5,9,8,15,23