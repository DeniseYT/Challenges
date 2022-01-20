# A pangram is a sentence that contains all the letters of the English alphabet at least once, like “The quick brown fox jumps over the lazy dog.”

# Write a function to check a sentence to see if it is a pangram or not.

# For example:
# >>> is_pangram("The quick brown fox jumps over the lazy dog!")
# True

# >>> is_pangram("I like cats, but not mice")
# False


# Start my solution:

# My solution 
def is_pangram(sentence):

    lower_sentence = sentence.lower()
    set_of_sentence = set(lower_sentence)
    # print(set_of_sentence)

    new_sentence = []

    for letter in set_of_sentence:
        if letter.isalpha():
            new_sentence.append(letter)
    # print(len(new_sentence))
    
    if len(new_sentence) == 26:
        return True
    
    return False

print(is_pangram("The quick brown fox jumps over the lazy dog!"))