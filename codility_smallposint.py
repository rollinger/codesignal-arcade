"""
Write a function:

    def solution(A)

that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

Write an efficient algorithm for the following assumptions:

        N is an integer within the range [1..100,000];
        each element of array A is an integer within the range [−1,000,000..1,000,000].
"""
def smallestPositiveInt(A):
	minimum = min(A)
	if minimum <= 0:
		return 1
	for i in sorted(A):
		if i-1 > 0 and i-1 not in A:
			return i-1
	maximum = max(A)
	if maximum < 1000000:
		return maximum+1

if __name__ == "__main__":
	def test(value, expect):
		test = smallestPositiveInt(value)
		if test != expect:
			print("MISTAKE %s != %s (value was %s)"%(test, expect, value))
		else:
			print("CORRECT %s == %s (value was %s)"%(test, expect, value))
	print("TESTS:")
	test([55,2,3,4,5], 1)
	test([44,3,22,48,765], 2)
	test([1, 3, 6, 4, 1, 2, 55], 5)
	test([1, 2, 3], 4)
	test([-1, -3], 1)