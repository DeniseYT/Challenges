Given list of chars, return a new copy, but with vowels replaced by *.

For example:
>>> replace_vowels(['h', 'i'])
['h', '*']

>>> replace_vowels(['o', 'o', 'o'])
['*', '*', '*']

>>> replace_vowels(['z', 'z', 'z'])
['z', 'z', 'z']

An empty list should return an empty list:
>>> replace_vowels([])
[]

Make sure to handle uppercase:
>>> replace_vowels(["A", "b"])
['*', 'b']

Do not consider y a vowel:
>>> replace_vowels(["y", "a", "y"])
['y', '*', 'y']

