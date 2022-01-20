In this challenge, you’ll write a function that is given a list of items and returns a new list of those items, in the same order, but with duplicate removed.

For example:
>>> deduped([1, 1, 1])
[1]

Keep items in the order where they first appeared:
>>> deduped([1, 2, 1, 1, 3])
[1, 2, 3]

A list with no duplicates would return the same:
>>> deduped([1, 2, 3])
[1, 2, 3]

This should return a new list, not mutate the existing list:
>>> a = [1, 2, 3]
>>> b = deduped(a)
>>> a == b
True
>>> a is b
False

An empty list should return an empty list:
>>> deduped([])
[]

