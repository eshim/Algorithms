"""
Mergesort

Split lists in sublists until they each contain 1 element, then
repeatedly merge sublists by comparing the smallest element in
each list and adding them to a merged list in order.

Worst Case Performance: O(n log n)
Best Case Performance: O(n log n)
Average Case Performance: O(n log n)
"""

def merge(array1, array2):
	merged_array = []
	while array1 or array2: # while those arrays exist
		if not array1: #if array one doesn't exist
			merged_array.append(array2.pop())
		elif (not array2) or array1[-1] > array2[-1]:
				# if array 2 doesn't exist, or if the last value of array1 is greater than the last value of array 2
			# print "ARRAY1[-1]", array1[-1]
			merged_array.append(array1.pop())
		else:
			# print "ARRAY2[-1]", array2[-1]

			merged_array.append(array2.pop())
	merged_array.reverse()
	# print merged_array
	return merged_array

def mergeSort(array):
	arrayLength = len(array)
	if arrayLength < 2:
		return array
	left = array[:arrayLength/2]
	right = array[arrayLength/2:]
	return merge(mergeSort(left), mergeSort(right))

# test
mylist = [0,10,3,2,11,22,40,-1,5]
print mergeSort(mylist)