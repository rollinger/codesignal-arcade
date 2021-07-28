"""
Given a sequence of integers as an array, determine whether it is possible to
obtain a strictly increasing sequence by removing no more than one element
from the array.

Note: sequence a0, a1, ..., an is considered to be a strictly increasing
if a0 < a1 < ... < an. Sequence containing only one element is also
considered to be strictly increasing.
"""
def almostIncreasingSequence_0(sequence):
	if len(sequence) <= 2:
		return True

	def increase(test):
		if len(test) == 2:
			return test[0] < test[1]

		else:
			for i in range(0, len(test)-1):
				if test[i] >= test[i+1]:
					return False
			return True

	for i in range (0, len(sequence) - 1):
		if sequence[i] >= sequence [i+1]:
			test_seq1 = sequence[:i] + sequence[i+1:]
			test_seq2 = sequence[:i+1] + sequence[i+2:]
			return increase(test_seq1) or increase(test_seq2)

def almostIncreasingSequence_1(sequence):
	ascSeq = []; seq = sequence;
	ascSeq.append(min(sequence[:2]))
	if (len(sequence) >= 2 and sequence[:2][0] > sequence[:2][1]):
		seq = sequence[1:]
	for i in seq:
		if ascSeq[-1] < i:
			ascSeq.append(i)
	if (len(sequence) - len(ascSeq)) > 1:
		return (False)
	return (True)

def almostIncreasingSequence_2(sequence):
	def is_ascending(seq):
		for i in range(0, len(seq)-1):
			if seq[i] >= seq[i+1]:
				return (False)
		return (True)

	if is_ascending(sequence) or len(sequence) <= 2:
		return True
	for d in range(0, len(sequence)):
		test = sequence.copy()
		del test[d]
		if is_ascending(test):
			return True
	return False

def almostIncreasingSequence(sequence):
	# Brute Force
	def copy(seq):
		r = seq[::]
		return r
	def is_ascending(seq):
		for i in range(0, len(seq)-1):
			if seq[i] >= seq[i+1]:
				return (False)
		return (True)

	if is_ascending(sequence) or len(sequence) <= 2:
		return True
	for d in range(0, len(sequence)):
		test = copy(sequence)
		del test[d]
		if is_ascending(test):
			return True
	return False


if __name__ == "__main__":
	def test(value, expect):
		test = almostIncreasingSequence(value);
		if test != expect:
			print("MISTAKE %s != %s (value was %s)"%(test, expect, value))
		else:
			print("CORRECT %s == %s (value was %s)"%(test, expect, value))
	print("TESTS:")
	test([1, 3, 2, 1], False)
	test([3], True)
	test([1, 3, 2], True)
	test([10, 1, 2, 3, 4, 5], True)
	test([0, -2, 5, 6], True)
	test([1, 2, 3, 4, 5, 3, 5, 6], False)
	test([40, 50, 60, 10, 20, 30], False)
	test([1, 2, 5, 3, 5], True)
	test([1, 2, 3, 4, 99, 5, 6], True)
