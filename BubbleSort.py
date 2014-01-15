"""
Bubblesort

Smaller elements "bubble" to the top.

Start from the beginnning of the list, compare adjacent elements
and swap if they are not in the correct order. After each iteration
one less element needs to be compared.

Is generally the worst algorithm due to writing so much.
Doesn't work well with modern CPU hardware.

Worst Case Performance: O(n^2)
Best Case Performance: O(n)
Average Case Performance: O(n^2)
"""


def bubblesort(inlist):
	for sublist in range(len(inlist), -1, -1):
		for x in range(0, sublist-1):
			if inlist[x] > inlist[x +1]:
				inlist[x], inlist[x+1] = inlist[x+1], inlist[x]
	return inlist

# test
mylist = [0,10,3,2,11,22,40,-1,5]
print bubblesort(mylist)
