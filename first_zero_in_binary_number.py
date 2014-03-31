"""
Algorithm to find the index of first zero in a binary number where index zero is furtherest right in array
"""
number = 20
bin_number = bin(number)
print "Number is %d" %number
print "Binary represendation is %s" %bin_number

def get_first_zero(bin_number):
	for i in reversed(range(len(bin_number))):
		if bin_number[i] == "1":
			return len(bin_number) - i
	return -1
print "Index of the first 1 is: %d" %get_first_zero(bin_number)



