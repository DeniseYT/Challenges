# Write a function, find_longest_word, that takes a list of words and returns the length of the longest one.

# # Examples
# >>> find_longest_word(["hi", "hello"])
# 5

# >>> find_longest_word(["Balloonicorn", "Hackbright"])
# 12


# Start my solution:

# My solution
def find_longest_word(words):

    largest = len(words[0])

    for word in words:
        if len(word) > largest:
            largest = len(word)
    
    return largest

    # list comprehension
    # return max([len(word) for word in words])

print(find_longest_word(["Balloonicorn", "Hackbright"]))