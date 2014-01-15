

def quicksortSimple(data):
    if len(data) < 2:
        return data

    pivotIndex = len(data) / 2
    pivotValue = data[pivotIndex]

    leftCount = 0
    
    for i in range(0, len(data)):
        if data[i] < pivotValue:
            i += 1

    left = []
    right = []
    
    for i in range (0, len(data)):
        # if i == pivotIndex:
        val = data[i]
        if val < pivotValue:
            left.append(val)
        elif val > pivotValue:
            right.append(val)

    left = quicksortSimple(left)
    right = quicksortSimple(right)

    newlist = left
    newlist.append(pivotValue)
    for value in right:
        newlist.append(value)

    print newlist
    return newlist

def quicksortShort(inlist):
	"""Easy to read quicksort, but allocates a lot of new lists"""
	if inlist == []:
		return []
	else:
		pivot = inlist[0]
		lesser = quicksortShort([x for x in inlist [1:] if x < pivot])
		greater = quicksortShort([x for x in inlist [1:] if x > pivot])
		return lesser + [pivot] + greater


def quicksortPartition(inlist):
	"""Quicksort using partition"""
	if inlist == []:
		return []
	else:
		pivot = inlist[0]
		lesser, equal, greater = partition(inlist[1:], [], [pivot], [])
		return quicksortPartition(lesser) + equal + quicksortPartition(greater)

def partition(inlist, larger, equal, greater):
	"""Function that helps sorting by grouping the equal pivot elements together"""
	while inlist != []:
		head = inlist.pop(0)
		if head < equal[0]:
			larger += [head] 
		elif head > equal[0]:
			greater += [head]
		else:
			equal += [head]
	return (larger, equal, greater)

def quicksortRecursive(mylist):
	pivot = mylist[len(mylist)/2]
	current_pos =0
	

mylist = [0,10,3,2,11,22,40,-1,5]

quicksortSimple(mylist)

print quicksortShort(mylist)

print quicksortPartition(mylist)