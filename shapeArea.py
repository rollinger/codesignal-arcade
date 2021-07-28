"""
Below we will define an n-interesting polygon. Your task is to find the area
of a polygon for a given n.

A 1-interesting polygon is just a square with a side of length 1.
An n-interesting polygon is obtained by taking the n - 1-interesting polygon
and appending 1-interesting polygons to its rim, side by side.
You can see the 1-, 2-, 3- and 4-interesting polygons in the picture below.
"""
def shapeArea(n):
	m = (n*n) + ( (n-1) * (n-1) )
	return (m)

if __name__ == "__main__":
	def test(value, expect):
		test = shapeArea(value);
		if test != expect:
			print("MISTAKE %d != %d (value was %s)"%(test, expect, value))
		else:
			print("CORRECT %d == %d (value was %s)"%(test, expect, value))
	print("TESTS:")
	test(1, 1)
	test(2, 5)
	test(3, 13)
	test(4, 25)
