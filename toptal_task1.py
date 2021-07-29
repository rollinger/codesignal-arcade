"""
Task 1

"""
def solution(S):
	def split_sentence(s):
		sarr = [] 
		l = 0
		for i,v in enumerate(s):
			if v in list(".!?"):
				sarr.append(s[l:i-1])
				l = i+1
		sarr.append(s[l:])
		return sarr
	larg_w_c = 0
	for s in split_sentence(S):
		sl = len(list(filter(None,s.split(" "))))
		if sl > larg_w_c:
			print(s)
			larg_w_c = sl 
	return larg_w_c

if __name__ == "__main__":
	def test(value, expect):
		test = solution(value)
		if test != expect:
			print("MISTAKE %s != %s (value was %s)"%(test, expect, value))
		else:
			print("CORRECT %s == %s (value was %s)"%(test, expect, value))
	print("TESTS:")
	test("Forget   CV's..Save time   ! x x", 2)
	test("Forget   C!!?:!!&DFV.'s..Save   H.e!l,;l o o *'# sup dup  time! x..x", 7)
	#test(3,0)
	