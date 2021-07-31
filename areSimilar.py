"""

"""
def areSimilar(a, b):
	l = [x == y for x,y in zip(a,b)]
	print(l)
	if l.count(False) > 2:
		return False
	elif l.count(False) == 2:
		#check if swap would solve it
		swap = [i for i, v in enumerate(l) if v == False]
		a[swap[0]], a[swap[1]] = a[swap[1]], a[swap[0]]
		l = [x == y for x,y in zip(a,b)]
		print(l)
		return l.count(False) == 0
	else:
		return True 
	return l.count(False) <= 2


if __name__ == "__main__":
	def test(value1, value2, expect):
		test = areSimilar(value1, value2)
		if test != expect:
			print("MISTAKE %s != %s (value was %s & %s)"%(test, expect, value1, value2))
		else:
			print("CORRECT %s == %s (value was %s & %s)"%(test, expect, value1, value2))
	print("TESTS:")
	test([1, 2, 3], [1, 2, 3], True)
	test([1, 2, 3],[2, 1, 3], True)

	test([1, 1, 4],[1, 2, 3], False)
	test([1, 2, 3],[1, 10, 2], False)
