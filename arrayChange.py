"""
You are given an array of integers. On each move you are allowed to 
increase exactly one of its element by one. 
Find the minimal number of moves required to obtain a 
strictly increasing sequence from the input.
"""
def arrayChange(inputArray):
	transform = inputArray.copy()
	moves = 0
	maximum = transform[0]
	for i in range(1,len(inputArray)):
		while transform[i] <= maximum:
			print(transform)
			transform[i] += 1
			moves += 1
		maximum = max(maximum,transform[i])
	print(transform)
	return moves


if __name__ == "__main__":
	def test(value, expect):
		test = arrayChange(value)
		if test != expect:
			print("MISTAKE %s != %s (value was %s)"%(test, expect, value))
		else:
			print("CORRECT %s == %s (value was %s)"%(test, expect, value))
	print("TESTS:")
	test([1, 1, 1], 3)
	test([-1000, 0, -2, 0], 5)
	#test("foo(bar)baz(blim)", "foorabbazmilb")
	#test("foo(bar(baz))blim", "foobazrabblim")
	