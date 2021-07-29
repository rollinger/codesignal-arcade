"""
BinaryGap
Find longest sequence of zeros in binary representation of an integer.


"""
def binaryGap(n):
	def tob(n):
		return bin(n)[2:] if n >= 0 else bin(n)[3:]
	bl = list(tob(n))
	longest = 0
	current = 0
	for bit in bl:
		#print("%s: %d"%(bit,current))
		if bit == '1': # ['1', '0', '0', '1']
			if current > 0:
				if longest <= current: longest = current
			current = 0
		elif bit == '0' and current >= 0:
			current += 1
	#print(bl)
	return longest

if __name__ == "__main__":
	def test(value, expect):
		test = binaryGap(value)
		if test != expect:
			print("MISTAKE %s != %s (value was %s)"%(test, expect, value))
		else:
			print("CORRECT %s == %s (value was %s)"%(test, expect, value))
	print("TESTS:")
	test(9, 2)
	test(529, 4)
	test(20,1)
	test(15,0)
	test(32,0)
	test(55, 1)
	test(3, 0)
	test(1111, 3)
	test(-23, 1)
	test(-10000234, 3)
	test(1008, 0)
	test(0, 0)
	test(1, 0)
	test(2147483647, 0)
	test(1147483647, 3)
	