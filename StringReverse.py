stringToReverse = "Reverse me!"

def typicalReverseString(stringInput):
	"""Reverses the string by making a new string for each character appended in reverse. Memory inefficient"""
	reversedString = "" 
	for index in range(len(stringInput) -1, -1, -1):
		reversedString += stringInput[index] # makes new strings again and again

	return reversedString

def listReverseString(stringInput):
	"""Reverses the string by adding each character to a list in reverse."""
	reversedList = []
	for index in range(len(stringInput) -1, -1, -1):
		reversedList.append(stringInput[index])

	return ''.join(reversedList)


def recursiveReverseStringWrapper(stringInput):
	"""Wrapper for following recursive function"""
	assert type(stringInput) == str, 'Make sure a string is input'
	assert len(stringInput) > 0, 'Make sure that that the string is not empty'
	stringTracker = ''
	return recursiveReverseString(stringInput, stringTracker)


def recursiveReverseString(stringInput, stringTracker):
	"""Tail recursive function to reverse a string. Loses efficiency to repeated function calls and allocation of strings"""
	if len(stringInput) > 0 :
		stringTracker += stringInput[-1] # still pretty inefficient to be remaking immutable data structures
		return recursiveReverseString(stringInput[:-1], stringTracker)
	else:
		return stringTracker
	

def fastReverseString(stringInput):
	"""Uses extended string slicing to cover the for loop"""
	return stringInput[::-1]
# print type('h')
print recursiveReverseStringWrapper(stringToReverse)
# recursiveReverseStringWrapper(1)