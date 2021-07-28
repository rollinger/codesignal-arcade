"""
Some people are standing in a row in a park. There are 
trees between them which cannot be moved. Your task is to 
rearrange the people by their heights in a non-descending 
order without moving the trees. People can be very tall!
"""
def sortByHeight(a):
	b = []
	for i,v in enumerate(a):
		if v != -1:
			b.append(v)
			a[i] = None
	b.sort()
	for i,v in enumerate(a):
		if not v:
			a[i] = b.pop(0)
	return a


if __name__ == "__main__":
	def test(value, expect):
		test = sortByHeight(value)
		if test != expect:
			print("MISTAKE %s != %s (value was %s)"%(test, expect, value))
		else:
			print("CORRECT %s == %s (value was %s)"%(test, expect, value))
	print("TESTS:")
	test([-1, 150, 190, 170, -1, -1, 160, 180],  [-1, 150, 160, 170, -1, -1, 180, 190])
	test([23, 54, -1, 43, 1, -1, -1, 77, -1, -1, -1, 3], [1, 3, -1, 23, 43, -1, -1, 54, -1, -1, -1, 77])