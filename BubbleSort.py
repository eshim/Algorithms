def bubblesort(inlist):
	# worst case performance = n^2
	# average case performance = n^2
	# best case performance = n
	# is generally the worst algorithm due to writing so much
	# doesn't work well with modern CPU hardware
	
	for sublist in range(len(inlist), -1, -1):
		for x in range(0, sublist-1):
			if inlist[x] > inlist[x +1]:
				inlist[x], inlist[x+1] = inlist[x+1], inlist[x]
	return inlist

mylist = [0,10,3,2,11,22,40,-1,5]

print bubblesort(mylist)
