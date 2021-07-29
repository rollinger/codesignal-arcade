"""
A non-empty array A consisting of N integers is given. 
The unique number is the number that occurs exactly once in array A.

You should find the first unique number in A. In other words, 
find the unique number with the lowest position in A.

Test passes, but the performance is bad for large sets using A.count(i)


"""
def firstunique(A):
	def is_unique(A,i):
		n = 0
		for x in A:
			if x == i:
				n += 1
			if n > 1:
				return False
		return True
	for i in A:
		if A.count(i) == 1:
			return i
	return -1

if __name__ == "__main__":
	def test(value, expect):
		test = firstunique(value)
		if test != expect:
			print("MISTAKE %s != %s (value was %s)"%(test, expect, value))
		else:
			print("CORRECT %s == %s (value was %s)"%(test, expect, value))
	print("TESTS:")
	test([4,10,5,4,2,10], 5)
	test([1,4,3,3,1,2], 4)
	test([6,4,4,6], -1)
	test([107, 371, 370, 929, 496, 802, 31, 416, 169, 395, 633, 398, 64, 519, 134, 691, 878, 217, 640, 888, 771, 718, 421, 114, 82, 285, 687, 572, 789, 376, 77, 632, 128, 615, 595, 384, 186, 165, 449, 966, 793, 454, 193, 383, 218, 203, 923, 952, 167, 476, 464, 458, 195, 655, 537, 674, 339, 660, 724, 619, 753, 415, 468, 817, 36, 508, 271, 806, 30, 997, 964, 669, 873, 142, 616, 926, 527, 846, 521, 345, 473, 712, 498, 429, 938, 423, 672, 961, 382, 210, 555, 313, 713, 153, 726, 276, 872, 153, 566], 107)
	test([7, 2, 2, 1, 10, 5, 10, 3, 10, 7], 1)
	