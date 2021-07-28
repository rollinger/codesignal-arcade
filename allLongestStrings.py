"""
Given an array of strings, return another array containing all of its longest strings.
"""
def allLongestStrings(inputArray):
	l = len(max(inputArray, key=len))
	longest = []
	for s in inputArray:
		if len(s) == l:
			longest.append(s)
	return longest

if __name__ == "__main__":
	def test(value, expect):
		test = allLongestStrings(value);
		if test != expect:
			print("MISTAKE %s != %s (value was %s)"%(test, expect, value))
		else:
			print("CORRECT %s == %s (value was %s)"%(test, expect, value))
	print("TESTS:")
	test(["aba", "aa", "ad", "vcd", "aba"], ["aba", "vcd", "aba"])
	test(["enyky", "benyky", "yely", "varennyky"], ["varennyky"])
