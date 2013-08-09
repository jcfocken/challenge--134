''' 
Solution to reddits daily programming challenge of the 8/6/13
http://www.reddit.com/r/dailyprogrammer/comments/1jtryq/080613_challenge_134_easy_ndivisible_digits/

Prints the highest N digit number divisible by M
'''

n = input("Enter a value for N: ")
m = input("Enter a value for M: ")

high_possible = (10 ** n)
low_possible = (10 ** (n - 1))

for i in reversed(range(low_possible, high_possible)):
	if (i % m == 0):
		print "Result: {}".format(i)
		break
else: print "No Solution"

