# https://leetcode.com/problems/longest-common-prefix/

# 14. Longest Common Prefix

# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.


def longest_common_prefix(strs):

    new_str = ""

    for a in zip(*strs):
        # print(a) 
        # ('f', 'f', 'f')
        # ('l', 'l', 'l')
        # ('o', 'o', 'i')
        # ('w', 'w', 'g')

        if (len(set(a))) == 1:
            new_str += a[0]
        else:
            break
    
    return new_str

print(longest_common_prefix(["flower","flow","flight"])) #fl
