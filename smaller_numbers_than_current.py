# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

# 1365. How Many Numbers Are Smaller Than the Current Number

# Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. 
# That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].
# Return the answer in an array.

# Example 1:
# Input: nums = [8,1,2,2,3]
# Output: [4,0,1,1,3]
# Explanation: 
# For nums[0]=8 there exist four smaller numbers than it (1, 2, 2 and 3). 
# For nums[1]=1 does not exist any smaller number than it.
# For nums[2]=2 there exist one smaller number than it (1). 
# For nums[3]=2 there exist one smaller number than it (1). 
# For nums[4]=3 there exist three smaller numbers than it (1, 2 and 2).

# Example 2:
# Input: nums = [6,5,4,8]
# Output: [2,1,0,3]

# Example 3:
# Input: nums = [7,7,7,7]
# Output: [0,0,0,0]


# My solution 1 
def smaller_numbers_than_current(nums):

    new_list = []

    for num1 in nums:
        count = 0 #歸0 each time, if we put outside of loop, will keep counting and never 歸0
        for num2 in nums:
            if num1 != num2 and num1 > num2:
                count += 1
        new_list.append(count)
    
    return new_list

print(smaller_numbers_than_current([8,1,2,2,3])) #[4, 0, 1, 1, 3]


# My solution 2 - dictionary
def smaller_numbers_than_current(nums):

    new_list = []
    new_dict = {}
    sort_nums = sorted(nums)
    #print(sort_nums) #[1, 2, 2, 3, 8]

    for i in range(len(sort_nums)):
        if sort_nums[i] not in new_dict:
            new_dict[sort_nums[i]] = i
    # print(new_dict) #{1: 0, 2: 1, 3: 3, 8: 4} #index=count

    for num in nums:
        new_list.append(new_dict[num])
    
    return new_list

print(smaller_numbers_than_current([8,1,2,2,3])) #[4, 0, 1, 1, 3]


# My solution 3 - enumerate
def smaller_numbers_than_current(nums):

    new_dict = {}

    for index, num in enumerate(sorted(nums)):
        new_dict.setdefault(num, index)
    #print(new_dict) #{1: 0, 2: 1, 3: 3, 8: 4}

    return [new_dict[num] for num in nums]
print(smaller_numbers_than_current([8,1,2,2,3]))


# My solution 4 - sort
def smaller_numbers_than_current(nums):

    new_list = []
    new_nums = sorted(nums)
    # print(new_nums) #[1, 2, 2, 3, 8] 
    
    for i in range(len(nums)):
        for j in range(len(new_nums)):
            if nums[i] == new_nums[j]:
                new_list.append(j)
                break
    
    return new_list

print(smaller_numbers_than_current([8,1,2,2,3])) #[4, 0, 1, 1, 3]


