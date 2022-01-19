# Define a function max_of_three that takes in three numbers as arguments and returns the largest of them.

# For example:
# >>> maxofthree(1, 5, 2)
# 5

# >>> maxofthree(10, 1, 11)
# 11


# Start my solution:

# My solution 1
def max_of_three(num1, num2, num3):

    largest = num1
    nums = (num1, num2, num3)

    for num in nums:
        if num > largest:
            largest = num
    
    return largest

print(max_of_three(1, 5, 2))


# My solution 2
def max_of_three(num1, num2, num3):

    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    elif num3 >= num1 and num3 >= num2:
        return num3
    else:
        return "no largest"

print(max_of_three(5, 5, 5))