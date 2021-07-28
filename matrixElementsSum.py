"""
Given a sequence of integers as an array, determine whether it is possible to
obtain a strictly increasing sequence by removing no more than one element
from the array.

Note: sequence a0, a1, ..., an is considered to be a strictly increasing
if a0 < a1 < ... < an. Sequence containing only one element is also
considered to be strictly increasing.
"""
def matrixElementsSum(matrix):
	def matrix_transform(matrix):
		idx_blk = []
		for i in range(0, len(matrix)):
			for j in range(0, len(matrix[0])):
				#print(matrix[i][j])
				if matrix[i][j] == 0:
					idx_blk.append(j)
				if j in idx_blk:
					matrix[i][j] = 0
		return matrix
	transform = matrix_transform(matrix)
	return sum(map(sum,transform))

if __name__ == "__main__":
	def test(value, expect):
		test = matrixElementsSum(value);
		if test != expect:
			print("MISTAKE %s != %s (value was %s)"%(test, expect, value))
		else:
			print("CORRECT %s == %s (value was %s)"%(test, expect, value))
	print("TESTS:")
	matrix = 	[[0, 1, 1, 2], 
        		[0, 5, 0, 0], 
          		[2, 0, 3, 3]]
	test(matrix, 9)
	matrix = [[1, 1, 1, 0], 
          [0, 5, 0, 1], 
          [2, 1, 3, 10]]
	test(matrix, 9)
	"""
	test([1, 3, 2, 1], False)
	test([3], True)
	test([1, 3, 2], True)
	test([10, 1, 2, 3, 4, 5], True)
	test([0, -2, 5, 6], True)
	test([1, 2, 3, 4, 5, 3, 5, 6], False)
	test([40, 50, 60, 10, 20, 30], False)
	test([1, 2, 5, 3, 5], True)
	test([1, 2, 3, 4, 99, 5, 6], True)
	test([1, 2, 3, 4, 3, 6], True)
	test([3, 5, 67, 98, 3], True)
	test([1, 1, 2, 3, 4, 4], False)
	"""