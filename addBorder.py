"""

"""
def addBorder(picture):
	framed = ['*'*(len(picture[0]) + 2)]
	for line in picture:
		framed.append('*'+line+'*')
	framed.append('*'*(len(picture[0]) + 2))
	return framed


if __name__ == "__main__":
	def test(value, expect):
		test = addBorder(value)
		if test != expect:
			print("MISTAKE %s != %s (value was %s)"%(test, expect, value))
		else:
			print("CORRECT %s == %s (value was %s)"%(test, expect, value))
	print("TESTS:")
	test(["abc","ded"], ["*****","*abc*","*ded*","*****"])
	