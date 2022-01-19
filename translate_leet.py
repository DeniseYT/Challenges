# in which standard letters are often replaced by numerals or special characters.

# Letter -> Becomes

# a -> @
# o -> 0
# e -> 3
# l -> 1
# s -> 5
# t -> 7

# In this exercise, you’ll make a function that translate a word to leet-speak:

# >>> translate_leet("Hi Balloonicorn")
# 'Hi B@1100nic0rn'

# >>> translate_leet("Hackbright is the Shizzle")
# 'H@ckbrigh7 i5 7h3 5hizz13'


# Start my solution:

# My solution 
def translate_leet(phrase):

    leet_speak = {
        "a": "@",
        "o": "0",
        "e": "3",
        "l": "1",
        "s": "5",
        "t": "7",
    }
    
    new_phrase = ""

    for letter in phrase:
        if letter == "a":
            letter = leet_speak["a"]
            new_phrase += letter

        elif letter == "o":
            letter = leet_speak["o"]
            new_phrase += letter

        elif letter == "e":
            letter = leet_speak["e"]
            new_phrase += letter
            
        elif letter == "l":
            letter = leet_speak["l"]
            new_phrase += letter
            
        elif letter == "s":
            letter = leet_speak["s"]
            new_phrase += letter
            
        elif letter == "t":
            letter = leet_speak["t"]
            new_phrase += letter
        
        else:
            new_phrase += letter
            
    return new_phrase

print(translate_leet("Hi Balloonicorn"))