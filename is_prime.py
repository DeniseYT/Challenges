# Write a function the returns True or False, depending on whether the integer passed into it is a prime number.

# Only numbers >1 can be prime numbers:
# >>> is_prime(0)
# False

# >>> is_prime(1)
# False

# Any number >1 that has no divisors other than 1 and itself is a prime number:
# >>> is_prime(2)
# True

# >>> is_prime(3)
# True

# >>> is_prime(4)
# False

# >>> is_prime(11)
# True

# >>> is_prime(999)
# False


# Start my solution:

# My solution 1
def is_prime(num):

    if num <= 1:
        return False
    
    elif num % 2 == 0 or num % 3 == 0 or num % 5 == 0 or num % 7 == 0:
        return False
    
    else:
        return True

print(is_prime(4))


# My solution 2
def is_prime(num):

    if num < 2:
        return False
    
    for n in range(2, num):
        if num % n == 0:
            return False
    
    return True

print(is_prime(999))