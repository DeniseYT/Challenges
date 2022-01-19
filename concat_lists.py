Given two lists. concatenate them (that is, combine them into a single list).
For example, given [1, 2] and [3, 4]:

# Examples
>>> concat_lists([1, 2], [3, 4])
[1, 2, 3, 4]

It should work if either list is empty:

# Examples
>>> concat_lists([], [1, 2])
[1, 2]

>>> concat_lists([1, 2], [])
[1, 2]

>>> concat_lists([], [])
[]