"""
Given two strings, find the number of common characters between them.
"""
def isLucky(n):
	nl = list(map(int, str(n)))
	half = len(nl)//2
	if (sum(nl[half:]) == sum(nl[:half])):
		return True
	return False


if __name__ == "__main__":
	def test(value, expect):
		test = isLucky(value)
		if test != expect:
			print("MISTAKE %s != %s (value was %s)"%(test, expect, value))
		else:
			print("CORRECT %s == %s (value was %s)"%(test, expect, value))
	print("TESTS:")
	test(1230, True)
	test(1231, False)