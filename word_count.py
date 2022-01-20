Given a phrase, print (not return) the word count in ascending order.

For example:
>>> word_count("berry cherry cherry cherry berry apple")
apple: 1
berry: 2
cherry: 3

If there is a tie for a count, make sure the words are printed in ascending order within the tie:
>>> word_count("hey hi hello")
hello: 1
hey: 1
hi: 1

Capitalized words are considered distinct:
>>> word_count("hi Hi hi")
Hi: 1
hi: 2


