# https://leetcode.com/problems/contains-duplicate/

# 217. Contains Duplicate

# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# Example 1:
# Input: nums = [1,2,3,1]
# Output: true

# Example 2:
# Input: nums = [1,2,3,4]
# Output: false

# Example 3:
# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true


# my solution 1
def contains_duplicate(nums):

    new_dict = {}
    count = 0

    for num in nums:
        if num not in new_dict:
            new_dict[num] = 1
        else:
            new_dict[num] += 1

    # print(new_dict) #{1: 2, 2: 1, 3: 1}
    # print(new_dict.values()) #dict_values([2, 1, 1]) / dict_values([1, 1, 1, 2])
    # print(new_dict.keys()) #dict_keys([2, 14, 18, 22])

    x = False

    for item in new_dict.values():
        if item > 1:
          return True

    return x #it should be putting outside of for loop, in case only check the first item and then return immediately and stop looping.

print(contains_duplicate([2,14,18,22,22])) 
        

# my solution 2     
def contains_duplicate(nums):

    new_dict = {}
    count = 0

    for num in nums:
        if num not in new_dict:
            new_dict[num] = 1
        else:
            new_dict[num] += 1

    for item in new_dict.keys():
        if new_dict[item] > 1: 
            return True
        
    return False #it should be putting outside of for loop, in case only check the first item and then return immediately and stop looping.
        

print(contains_duplicate([2,14,18,22,22]))

