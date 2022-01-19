# Given a word, return True if that word contains only unique characters. Return False otherwise.

# >>> has_unique_chars("Monday")
# True

# >>> has_unique_chars("Moonday")
# False

# >>> has_unique_chars("")
# True

# Uppercase and lowercase letters should be considered separately:

# >>> has_unique_chars("Bob")
# True


# Start my solution:

# Option 1
def has_unique_chars(word):

    letter_count = {}

    for letter in word:
        if letter not in letter_count:
            letter_count[letter] = 1
        else:
            letter_count[letter] += 1

    # print(letter_count)
    # print(letter_count.values())
    
    for item in letter_count.values():
        if item % 2 <= 1:
            return True
        else:
            return False
    
print(has_unique_chars("Monday"))


