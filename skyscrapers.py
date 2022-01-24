# You are given the heights of a row of buildings, from left to right, represented in an array of positive integers. A building is defined as a skyscraper if its height is strictly greater than both its neighbors. Compute and return the number of skyscrapers in this row of buildings.

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



# Solution 1
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



# Solution 2
# Show counts and indices of the skyscrapers

# Pseudocode:
# set a variable for counting the skyscrapers. we start it from 0.
# set a variable for storing the skyscrapers' indices. 
# iterate through the list except index[0] and index[-1] since the skyscrapers should have both sides of its neighbors.
# check if index is not yet in the set.
# increment by 1 if the condition is met.

def find_skyscrapers(lst):
    """Find how many skyscrapers of a row of buildings"""

    count = 0
    sky_index = set() 
    #store in a set - runtime O(1) when checking which building is in it.
    #store in a list - runtime O(n) when checking which building is in it since we need to check from the beginning.

    for i in range(1, len(lst)-1):
        if i not in sky_index:
            if lst[i] > lst[i-1] and lst[i] > lst[i+1]:
                sky_index.add(i)
                count += 1
    
    # print(count)
    # print(sky_index)

    return f"Total {count} skyscrapers, they are index of {sky_index}"
               
print(find_skyscrapers([2,3,1,3,1]))



# Solution 3
# Show counts and indices of the skyscrapers, index[0] and index[-1] can be skyscrapers too.
def find_skyscrapers(lst):
    """Find how many skyscrapers of a row of buildings"""
    
    count = 0
    sky_index = set() 
    #store in a set - runtime O(1) when checking which building is in it.
    #store in a list - runtime O(n) when checking which building is in it since we need to check from the beginning.

    if lst[0] > lst[1]:
        sky_index.add(0)
        count += 1
    
    if lst[-1] > lst[-2]:
        sky_index.add(-1)
        count += 1

    for i in range(1, len(lst)-1):
        if i not in sky_index:
            if lst[i] > lst[i-1] and lst[i] > lst[i+1]:
                sky_index.add(i)
                count += 1
    
    # print(count)
    # print(sky_index)

    return f"Total {count} skyscrapers, they are index of {sky_index}"
               
print(find_skyscrapers([4,3,5,2,6]))

