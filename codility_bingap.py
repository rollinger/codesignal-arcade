"""
BinaryGap
Find longest sequence of zeros in binary representation of an integer.


"""
def binaryGap(n):
	b = bin(n)[2:]
	return b

if __name__ == "__main__":
	def test(value, expect):
		test = binaryGap(value)
		if test != expect:
			print("MISTAKE %s != %s (value was %s)"%(test, expect, value))
		else:
			print("CORRECT %s == %s (value was %s)"%(test, expect, value))
	print("TESTS:")
	test([55,2,3,4,5], 1)
	test([44,3,22,48,765], 2)
	test([1, 3, 6, 4, 1, 2, 55], 5)
	test([1, 2, 3], 4)
	test([-1, -3], 1)