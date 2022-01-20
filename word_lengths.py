# Given a phrase, return dictionary keyed by word-length, with the value for each length being the set of words of that length.

# For example:
# >>> answer = word_lengths("cute cats chase fuzzy rats")

# This should return {4: {'cute', 'cats', 'rats'}, 5: {'chase', 'fuzzy'}}, but since both dictionaries and sets are unordered, 
# we can’t just check if it matches that exact string, so we’ll test more carefully:
# >>> sorted(answer.keys())
# [4, 5]
# >>> answer[4] == {'cute', 'cats', 'rats'}
# True
# >>> answer[5] == {'chase', 'fuzzy'}
# True

# Punctuation should be considered part of a word, so you only need to split the string on whitespace:
# >>> answer = word_lengths("Hi, I'm Balloonicorn")

# >>> sorted(answer.keys())
# [3, 12]

# >>> answer[3] == {'Hi,', "I'm"}
# True

# >>> answer[12] == {"Balloonicorn"}


# Start my solution:

# My solution 1
def word_lengths(sentence):

    new_dict = {}
    new_sentence = sentence.split()
    # print(new_sentence) #['cute', 'cats', 'chase', 'fuzzy', 'rats']

    for word in new_sentence:
        if len(word) not in new_dict:
            new_dict[len(word)] = set()
        #     new_dict[len(word)].add(word)
        # else:
        #     new_dict[len(word)].add(word)
        
        new_dict[len(word)].add(word) #add to value
        # no matter what, still need to add word

    return new_dict
    
print(word_lengths("cute cats chase fuzzy rats"))



