"""
ThreeLetters

Given two integers A and B, return a string which contains A letters "a" 
and B letters "b" with no three consecutive letters being the same.

"""
def threeletters(A,B):
	str = []
	while A > 0 and B > 0:
		
	return "".join(str)

if __name__ == "__main__":
	def test(value, expect):
		test = firstunique(value)
		if test != expect:
			print("MISTAKE %s != %s (value was %s)"%(test, expect, value))
		else:
			print("CORRECT %s == %s (value was %s)"%(test, expect, value))
	print("TESTS:")
	test(0,0, "")
	test(3,5, "")
	test(1,3, "")
	test(0,3, "")
	test(1,1, "")
	