"""
Ratiorg got statues of different sizes as a present from CodeMaster for his
birthday, each statue having an non-negative integer size. Since he likes to
 make things perfect, he wants to arrange them from smallest to largest so that
 each statue will be bigger than the previous one exactly by 1. He may need
 some additional statues to be able to accomplish that. Help him figure out
 the minimum number of additional statues needed.
"""
def makeArrayConsecutive2(statuses):
	remain = max(statuses) - min(statuses) - len(statuses) + 1
	return (remain)

if __name__ == "__main__":
	def test(value, expect):
		test = makeArrayConsecutive2(value);
		if test != expect:
			print("MISTAKE %d != %d (value was %s)"%(test, expect, value))
		else:
			print("CORRECT %d == %d (value was %s)"%(test, expect, value))
	print("TESTS:")
	test([6, 2, 3, 8], 3)
	test([6, 2, 3, 8, 4], 2)
	test([7, 6, 2, 3, 8, 4], 1)
	test([7, 6, 2, 3, 5, 8, 4], 0)
