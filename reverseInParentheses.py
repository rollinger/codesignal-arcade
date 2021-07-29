"""
Write a function that reverses characters in (possibly nested) parentheses 
in the input string.

Input strings will always be well-formed with matching ()s.
"""
def reverseInParentheses(inputString):
	def reverse(str, open, close):	
		lstr = str[:open]
		rstr = str[close+1:]
		rev = str[open+1:close][::-1]
		return ''.join([lstr,rev,rstr])
	def token(inputString):
		open = None; close = None
		for i,v in enumerate(inputString):
			if v == '(':
				open = i
			elif v == ')':
				close = i
				break
		if open >= 0 and close >= 0:
			inputString = reverse(inputString,open,close)
			#print("%s %s = %s"%(open,close, inputString))
		if '(' in list(inputString):
			inputString = token(inputString)
		return inputString
	return (token(inputString))


if __name__ == "__main__":
	def test(value, expect):
		test = reverseInParentheses(value)
		if test != expect:
			print("MISTAKE %s != %s (value was %s)"%(test, expect, value))
		else:
			print("CORRECT %s == %s (value was %s)"%(test, expect, value))
	print("TESTS:")
	test("(bar)", "rab")
	test("foo(bar)baz", "foorabbaz")
	test("foo(bar)baz(blim)", "foorabbazmilb")
	test("foo(bar(baz))blim", "foobazrabblim")
	