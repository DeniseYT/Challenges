# Return True/False if this word is a palindrome. A palindrome is a word that is spelled the same backwards and forwards.
# >>> is_palindrome("a")
# True

# >>> is_palindrome("noon")
# True

# >>> is_palindrome("racecar")
# True

# >>> is_palindrome("porcupine")
# False

# Treat spaces and uppercase letters normally—so “Racecar” wouldn’t be a palindrome since “R” and “r” aren’t the same letter:
# >>> is_palindrome("Racecar")
# False


# Start my solution:

# My solution 1
def is_palindrome(word):

    for i in range(len(word) // 2):
        # print(word[i])
        if word[i] != word[-i - 1]:
            # print("i:", word[i])
            # print(word[-i - 1])
            return False

    return True

print(is_palindrome("noon"))