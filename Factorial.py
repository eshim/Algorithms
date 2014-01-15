import math 
import bisect

def factorial(n, results):
	if n > 1:
		result =  factorial (n-1, results) * n
		results.append(result)
		return result
	else:
		result = 1
		results.append(result)
		return result

def wrapperFunction(n):
	results = []
	print factorial(n, results)
	print results

def factorialTail(n, accumulator):
	if n > 1:
		return factorialTail(n-1, accumulator * n)
	else:
		return accumulator

def factorialLoop(n):
	if n > 1:
		product = 1
		for i in range (1, n + 1):
			# print product
			# print "i" , i
			product *= i
		return product	
	else:
		return 1


print factorialTail(4, 1)
# wrapperFunction(500)
# print factorialLoop(8)

#binary search
myList = range(1,30)
# arange = float(9)/float(2)
# center = math.ceil(arange)
# print center
# print int(math.ceil(float(20)/2))
def binarySearch(aList, value, listMin = 0 , listMax = None):
	listMax = listMax if listMax is not None else len(aList)
	print listMax
	print listMin
	listRange = listMax - listMin
	if listRange < 0: # check values
		raise ValueError("List boundaries reversed.")

	position = (listRange / 2) + listMin
	# print position
	# print type(position)
	if value == aList[position]:
		return position
	elif value > aList[position]:
		return binarySearch(aList,value,  position + 1, listMax)
	elif value < aList[position]:
		return binarySearch(aList, value, listMin, position)
	elif listRange == 0:
		return -1

# There's also a bisect_left method, apparently.
# print bisect.bisect_left(myList, 10)



# def binary_search(value, items, low=0, high=None):
#     """
#     Binary search function.
#     Assumes 'items' is a sorted list.
#     The search range is [low, high)
#     """

#     high = len(items) if high is None else high
#     pos = low + (high - low) / 2

#     if pos == len(items):
#         return False
#     elif items[pos] == value:
#         return pos
#     elif high == low:
#         return False
#     elif items[pos] < value:
#         return binary_search(value, items, pos + 1, high)
#     else:
#         assert items[pos] > value
#         return binary_search(value, items, low, pos)

# def binarySearch(aList, n, listMin = 0, listMax = None):
# 	if listMax is None:
# 		 listMax = len(aList)

# 	while listMax > listMin:
# 		# print listMax
# 		# print listMin
# 		pos = (listMax + listMin)/2 
# 		# print aList[pos]
# 		if n == aList[pos]:
# 			return pos
# 		elif n > aList[pos]:
# 			listMin = pos + 1
# 		elif n < aList[pos]:
# 			listMax = pos
# 	return -1


# index = binarySearch(myList, 22, 0, 25) # list boundaries reversed
# print index
