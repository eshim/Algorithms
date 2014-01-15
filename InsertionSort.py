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


mylist = [0,10,3,2,11,22,40,-1,5]

print insertionSort(mylist)