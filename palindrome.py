"""
Given the string, check if it is a palindrome.

Example

    For inputString = "aabaa", the output should be
    checkPalindrome(inputString) = true;
    For inputString = "abac", the output should be
    checkPalindrome(inputString) = false;
    For inputString = "a", the output should be
    checkPalindrome(inputString) = true.

"""
def checkPalindrome(inputString):
	return (inputString[::-1] == inputString)

if __name__ == "__main__":
	def test(value, expect):
		test = checkPalindrome(value);
		if test != expect:
			print("MISTAKE %d != %d (value was \"%s\")"%(test, expect, value))
		else:
			print("CORRECT %d == %d (value was \"%s\")"%(test, expect, value))
	print("TESTS:")
	test("aabaa", True)
	test("abac", False)
	test("a", True)
