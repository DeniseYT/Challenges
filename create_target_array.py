# https://leetcode.com/problems/create-target-array-in-the-given-order/

# 1389. Create Target Array in the Given Order

# Given two arrays of integers nums and index. Your task is to create target array under the following rules:

# Initially target array is empty.
# From left to right read nums[i] and index[i], insert at index index[i] the value nums[i] in target array.
# Repeat the previous step until there are no elements to read in nums and index.
# Return the target array.

# It is guaranteed that the insertion operations will be valid.

# Example 1:
# Input: nums = [0,1,2,3,4], index = [0,1,2,2,1]
# Output: [0,4,1,3,2]
# Explanation:
# nums       index     target
# 0            0        [0]
# 1            1        [0,1]
# 2            2        [0,1,2]
# 3            2        [0,1,3,2]
# 4            1        [0,4,1,3,2]

# Example 2:
# Input: nums = [1,2,3,4,0], index = [0,1,2,3,0]
# Output: [0,1,2,3,4]
# Explanation:
# nums       index     target
# 1            0        [1]
# 2            1        [1,2]
# 3            2        [1,2,3]
# 4            3        [1,2,3,4]
# 0            0        [0,1,2,3,4]

# Example 3:
# Input: nums = [1], index = [0]
# Output: [1]

# My solution 1
def create_target_array(nums, index):

    target = []

    for i in range(len(index)):
        x = nums[i]
        y = index[i]
        # print(x)
        # print(y)
        # print("__")
        target.insert(y, x)
    
    return target

print(create_target_array([0,1,2,3,4], [0,1,2,2,1]))


# My solution 2
def create_target_array(nums, index):

    target = []

    for i, j in zip(index, nums): #zip function helps in assigning two values based on two list
        target.insert(i,j) #insert function helps in placing the desired value at desired location
    
    return target

print(create_target_array([0,1,2,3,4], [0,1,2,2,1]))