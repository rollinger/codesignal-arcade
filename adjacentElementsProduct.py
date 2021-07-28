"""
Given an array of integers, find the pair of adjacent elements that has
the largest product and return that product.

Example

For inputArray = [3, 6, -2, -5, 7, 3], the output should be
adjacentElementsProduct(inputArray) = 21.

7 and 3 produce the largest product.
"""
def adjacentElementsProduct(inputArray):
	products = []
	for i in (range(len(inputArray) - 1)):
		products.append(inputArray[i] * inputArray[i+1])
	return (max(products))

if __name__ == "__main__":
	def test(value, expect):
		test = adjacentElementsProduct(value);
		if test != expect:
			print("MISTAKE %d != %d (value was %s)"%(test, expect, value))
		else:
			print("CORRECT %d == %d (value was %s)"%(test, expect, value))
	print("TESTS:")
	test([3, 6, -2, -5, 7, 3], 21)
	test([4, 5, -2, -100, -3, 3], 300)
	test([77,22,9,3,4,2,5,2], 1694)
