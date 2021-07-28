"""
Given two strings, find the number of common characters between them.
"""
def commonCharacterCount(s1, s2):
	ls1 =  list(s1)
	ls2 =  list(s2)
	cc = list(set(s1) & set(s2))
	ccc = 0
	for c in cc:
		ccc += min(ls1.count(c),ls2.count(c))
	return ccc


if __name__ == "__main__":
	def test(value1, value2, expect):
		test = commonCharacterCount(value1, value2);
		if test != expect:
			print("MISTAKE %s != %s (value was %s | %s)"%(test, expect, value1, value2))
		else:
			print("CORRECT %s == %s (value was %s | %s)"%(test, expect, value1, value2))
	print("TESTS:")
	test("aabcc", "adcaa", 3)