# https://leetcode.com/problems/shuffle-the-array/

# 1470. Shuffle the Array

# Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].
# Return the array in the form [x1,y1,x2,y2,...,xn,yn].

# Example 1:
# Input: nums = [2,5,1,3,4,7], n = 3
# Output: [2,3,5,4,1,7] 
# Explanation: Since x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 then the answer is [2,3,5,4,1,7].

# Example 2:
# Input: nums = [1,2,3,4,4,3,2,1], n = 4
# Output: [1,4,2,3,3,2,4,1]

# Example 3:
# Input: nums = [1,1,2,2], n = 2
# Output: [1,2,1,2]


# My solution 1
def shuffle_array(nums, n):

    shuffle_list = []
    new_list_1 = nums[:n]
    new_list_2 = nums[n:]

    for i in range(n):
        shuffle_list.extend([new_list_1[i], new_list_2[i]])
        
    return shuffle_list

print(shuffle_array([2,5,1,3,4,7], 3)) #[2,3,5,4,1,7] 


# My solution 2
def shuffle_array(nums, n):

    new_list = []
    # n = len(nums)//2

    for i in range(n):
        new_list += [nums[i], nums[n]]
        n += 1
    
    return new_list

print(shuffle_array([2,5,1,3,4,7], 3)) #[2,3,5,4,1,7] 