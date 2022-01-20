# Write a function to turn a phrase into Pig Latin.
# Your function will be given a phrase (of one or more space-separated words). There will be no punctuation in it. You should turn this into the same phrase in Pig Latin.

# Rules
# If the word begins with a consonant (not a, e, i, o, u), move the first letter to the end and add ‘ay’
# If the word begins with a vowel, add ‘yay’ to the end

# For example:
# >>> pig_latin('porcupines are cute')
# 'orcupinespay areyay utecay'

# >>> pig_latin('give me an apple')
# 'ivegay emay anyay appleyay'


# Start my solution:

# My solution 
def pig_latin(phrase):

    new_phrase = phrase.split()
    # print(new_phrase) #convert to a list - ['give', 'me', 'an', 'apple']

    pig_latin = ""
    vowels = {"a", "e", "i", "o", "u"}

    for word in new_phrase:
        # print(word) #give #me #an #apple
        # print(word[0]) #g #m #a #a

        if word[0] in vowels:
            word += "yay"
            # print(word) #areyay
            pig_latin += word + " "
            
        elif word[0] not in vowels:
            word = word[1:] + word[0] + "ay"
            pig_latin += word + " "
    
    return pig_latin
            
print(pig_latin('give me an apple'))