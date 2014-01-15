"""
Insertion Sort

Take the last value of a list and compare it to each element
of the sorted sublist and places it accordingly until there 
are no more elements of the given list.


Worst Case Performance: O(n^2) comparisons and swaps
Best Case Performance: O(n) comparisons, O(1) swaps
Average Case Performance: O(n^2) comparisons and swaps
"""

def insertionSort(inlist):
	inlistLength = len(inlist)

	for i in range(inlistLength):
		sorting_value = inlist[i]
		j = i - 1
		while j >= 0 and inlist[j] > sorting_value:
			inlist[j+1] = inlist[j]
			j -= 1
		inlist[j+1] = sorting_value

	return inlist

def insertionSort2(inlist):
	inlistLength = len(inlist)

	for i in range(inlistLength):
		sorting_value = inlist[i]
		for j in range(i - 1, -1, -1):
			if inlist[j] > sorting_value:
				inlist[j+1] = inlist[j]
		inlist[j+1] = sorting_value

	return inlist

# test
mylist = [0,10,3,2,11,22,40,-1,5]

print insertionSort(mylist)