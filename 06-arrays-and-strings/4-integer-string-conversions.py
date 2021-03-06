def str_2_int(s):
	sign = 1
	result = 0
	if s[0] == "-":
		sign = -1
	else:
		result += int(s[0])
	for i in xrange(1, len(s)):
		result += pow(10,i) * int(s[i])
	return result * sign 


print str_2_int("-245")
print str_2_int("0")
print str_2_int("854930")


def int_2_str(x):
	result = ""
	if x == 0:
		return "0"
	elif x<0:
		result = "-"
		x = -x
	while x != 0:
		digit = x % 10	
		result = result + str(digit)
		x = (x - digit) / 10
	return result


print int_2_str(-584390)
print int_2_str(0)
print int_2_str(8594203)
