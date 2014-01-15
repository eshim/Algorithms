"""
Selection Sort 
Find the smallest element of the list and swap it to the first index, 
then search the list, without the first element and repeat until the
sublist is 0.
"""

mylist = [0,10,3,3,3,2,11,22,40,-1,5]

def selectionsort(inlist):
	for sublistStart in range(len(inlist)):
		# keep checking smaller lists within this list
		min_value = min(inlist[sublistStart:]) # min() finds the smallest value
		min_index = inlist[sublistStart:].index(min_value) # find index for min value relative to sublist
		if min_index != 0:
			# print inlist[sublistStart + min_index], inlist[sublistStart]
			inlist[sublistStart + min_index], inlist[sublistStart] = inlist[sublistStart], min_value #swap values
		print inlist
	return inlist


# stable - as in, elements with equal values should be placed in the same order that they are given, relative to each other

def selectionsort2(inlist):
	for sublist in range(len(inlist)):
		# keep checking smaller lists within this list
		min_index = sublist
		for sublistStart in range(sublist, len(inlist)):
			if inlist[min_index] > inlist[sublistStart]:
				min_index = sublistStart
		inlist.insert(sublist, inlist.pop(min_index))
		# min_index = inlist[sublistStart:].index(min_value) # find index for min value relative to sublist
		# if min_index != 0:
		# 	# print inlist[sublistStart + min_index], inlist[sublistStart]
		# 	inlist[sublistStart + min_index], inlist[sublistStart] = inlist[sublistStart], min_value #swap values
		print inlist
	return inlist
print selectionsort(mylist)