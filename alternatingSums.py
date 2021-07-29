"""
Several people are standing in a row and need to be divided into two teams. 
The first person goes into team 1, the second goes into team 2, 
the third goes into team 1 again, the fourth into team 2, and so on.

You are given an array of positive integers - the weights of the people. 
Return an array of two integers, where the first element is the total weight of 
team 1, and the second element is the total weight of team 2 after the division 
is complete.
"""
def alternatingSums(a):
	return [
		sum(map(int, [v for i,v in enumerate(a) if i%2==0])), 
		sum(map(int, [v for i,v in enumerate(a) if i%2==1]))
	]

if __name__ == "__main__":
	def test(value, expect):
		test = alternatingSums(value)
		if test != expect:
			print("MISTAKE %s != %s (value was %s)"%(test, expect, value))
		else:
			print("CORRECT %s == %s (value was %s)"%(test, expect, value))
	print("TESTS:")
	test([1,2,3,4,5,6,7,8,9,0], [25,20])
	test([50, 60, 60, 45, 70], [180,105])
	
	