Write a function to turn a phrase into Pig Latin.
Your function will be given a phrase (of one or more space-separated words). There will be no punctuation in it. You should turn this into the same phrase in Pig Latin.

Rules
If the word begins with a consonant (not a, e, i, o, u), move the first letter to the end and add ‘ay’
If the word begins with a vowel, add ‘yay’ to the end

For example:
>>> pig_latin('porcupines are cute')
'orcupinespay areyay utecay'

>>> pig_latin('give me an apple')
'ivegay emay anyay appleyay'