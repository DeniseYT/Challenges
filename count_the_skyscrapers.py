# You are given the heights of a row of buildings, from left to right, represented in an array of positive integers. 
# A building is defined as a skyscraper if its height is strictly greater than both its neighbors. 
# Compute and return the number of skyscrapers in this row of buildings.

# Assumptions:
# The input array will be integer based data and no other data types.
# Sample Input/Output

# Input: [1,1,1]
# Output: 0

# Input: [1,2,1]
# Output: 1

# Input: [1,3,1]
# Output: 1

# Input: [2,3,1,9]
# Output: 1

# Input: [2,3,1,9,4,5,4] 
# Output: 3

# Input: [5,4,3,2,1]
# Output: 0



# Solution 
# runtime: O(n), because we go through the list one time in each element.

# Pseudocode:
# set a variable for counting the skyscrapers. we start it from 0.
# iterate through the list except index[0] and index[-1] since the skyscrapers should have both sides of its neighbors.
# increment by 1 if the condition is met.

def find_skyscrapers(lst):
    """Find how many skyscrapers of a row of buildings"""

    count = 0

    for i in range(1, len(lst)-1):
        if lst[i] > lst[i-1] and lst[i] > lst[i+1]:
            count += 1
    
    return count

print(find_skyscrapers([2,3,1,9,4,5,4]))
