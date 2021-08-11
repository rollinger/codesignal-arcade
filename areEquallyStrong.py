"""
Call two arms equally strong if the heaviest weights they each are able to lift are equal.

Call two people equally strong if their strongest arms are equally strong (the strongest arm can be both the right and the left), and so are their weakest arms.

Given your and your friend's arms' lifting capabilities find out if you two are equally strong.
"""

def areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight):
	yourStongest = max(yourLeft, yourRight)
	yourWeakest = min(yourLeft, yourRight)
	friendsStrongest = max(friendsLeft, friendsRight)
	friendsWeakest = min(friendsLeft, friendsRight)
	return (yourStongest == friendsStrongest) and (yourWeakest == friendsWeakest)


if __name__ == "__main__":
	def test(value, expect):
		test = areEquallyStrong(value[0],value[1],value[2],value[3]);
		if test != expect:
			print("MISTAKE %s != %s (value was \"%s\")"%(test, expect, value))
		else:
			print("CORRECT %s == %s (value was \"%s\")"%(test, expect, value))
	print("TESTS:")
	test([20,15,5,20], False)
	test([15,10,15,9], False)
	test([15,10,15,10], True)
	test([10,15,15,10], True)
