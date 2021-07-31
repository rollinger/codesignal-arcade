"""
Given a string, find out if its characters can be rearranged to form a palindrome.

map the characters a to a count hash table. It can be rearranged if
maximum one char has an uneven sum
"""
def checkPalindrome(inputString):
	return (inputString[::-1] == inputString)

def palindromeRearranging(inputString):
	def charHash(str):
		map = {}
		for v in str:
			map[v] = map.get(v, 0) + 1
		return map
	def ispotentialPalindrome(map):
		uneven = 0
		for k,v in map.items():
			uneven += (v%2)
			if uneven > 1:
				return False
		return True
	map = charHash(inputString)
	print(map)
	return ispotentialPalindrome(map)

if __name__ == "__main__":
	def test(value, expect):
		test = palindromeRearranging(value);
		if test != expect:
			print("MISTAKE %s != %s (value was \"%s\")"%(test, expect, value))
		else:
			print("CORRECT %s == %s (value was \"%s\")"%(test, expect, value))
	print("TESTS:")
	test("aabb", True)
	test("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaabc", False)
	test("abbcabb", True)
