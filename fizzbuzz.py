# Write a program that counts from 1 to 20 in fizzbuzz fashion.

# To do so, loop from 1 to 20 (inclusive). Each time through, if the number is evenly divisible by 3, say ‘fizz’. 
# If the number is evenly divisible by 5, say ‘buzz’. 
# If the number is evenly divisible by both 3 and 5, say ‘fizzbuzz’. 
# Otherwise, say the number.

# For example:
# >>> fizzbuzz()
# 1
# 2
# fizz
# 4
# buzz
# fizz
# 7
# 8
# fizz
# buzz
# 11
# fizz
# 13
# 14
# fizzbuzz
# 16
# 17
# fizz
# 19
# buzz


# Start my solution:

def fizzbuzz():

    for i in range(1,21):
        if i % 15 == 0:
            print("fizzbuzz")
        elif i % 5 == 0:
            print("buzz")
        elif i % 3 == 0:
            print("fizz")
        else:
            print(i)
    
fizzbuzz()