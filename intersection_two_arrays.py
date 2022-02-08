# https://leetcode.com/problems/intersection-of-two-arrays-ii/

# 350. Intersection of Two Arrays II

# Given two integer arrays nums1 and nums2, return an array of their intersection. 
# Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

# Example 1:
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]

# Example 2:
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [4,9]
# Explanation: [9,4] is also accepted.


# My solution
def intersect(nums1, nums2):

    new_list = []

    for num_1 in nums1:
        if num_1 in nums2:
            new_list.append(num_1)
            nums2.remove(num_1) #avoid cheking the same item multiple times
            # print(nums2)
    
    return new_list
        
print(intersect([1,2,2,1], [2]))