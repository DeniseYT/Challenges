# Given a word in English, return True if that word contains more vowels than non-vowels; 
# otherwise, return False. 
# The word will always be a single word, without any punctuation or spaces. It will contain only uppercase and lowercase letters.

# If the phrase is over half vowels, it should return True:
# >>> has_more_vowels("moose")
# True

# If it’s half vowels (or less), it’s false:
# >>> has_more_vowels("mice")
# False

# >>> has_more_vowels("graph")
# False

# Don’t consider “y” as a vowel:
# >>> has_more_vowels("yay")
# False

# Uppercase vowels are still vowels:
# >>> has_more_vowels("Aal")
# True


# Start my solution:

# Option 1
def has_more_vowels(word):

    vowels = {"a", "e", "i", "o", "u"}
    lower_word = word.lower()
    have_vowel = 0
    no_vowel = 0

    for letter in lower_word:
        if letter in vowels:
            have_vowel += 1
        else:
            no_vowel += 1
    
    if have_vowel > no_vowel:
        return True
    elif have_vowel <= no_vowel:
        return False

print(has_more_vowels("Aal"))


