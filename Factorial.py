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


# print factorialTail(4, 1)
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



index = binarySearch(myList, 22, 0, 25) # list boundaries reversed
print index
