def permute2(s):
    res = []
    if len(s) == 1:
    	# base case
        res = [s] # if only one letter, return it
    else:
    	# recursive step
    	for i, c in enumerate(s): # for each starting letter
    		for perm in permute2(s[:i] + s[i+1:]): # find each permutation for the next letter
    			print "{0},{1}".format(s[:i], s[i+1:])
    			res += [c + perm]
    			print res

    return res # return a list of the possibilities

print permute2("hel")

print "hel"[:] , "hel"[1:]

# base case
# if only one letter
	# return the letter
# recursive step
# else
# find