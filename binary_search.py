Binary search is one of the most important Computer Science algorithms. It allows you to search a sorted list in O(log n) time, 
a large improvement over scanning every item in the list (which would be O(n) time).

To do this, you examine the middle item and, if the sought-for value is smaller, 
move halfway to the left. If the sought-after value is larger, move halfway to the right.

In this challenge, you’ll make binary search for the classic children’s guessing game of “pick a number from 1 to 100”.

Since you use binary search, it will never take more than 7 guesses for a function to find a number in the range 1 to 100 
(since log2 100) is just a little under 7).

For example:
>>> binary_search(50)
1
>>> binary_search(25)
2
>>> binary_search(75)
2
>>> binary_search(31) <= 7
True
>>> max([binary_search(i) for i in range(1, 101)])
7
