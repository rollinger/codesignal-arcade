"""
Task 3

"""
def solution(A):
	def compile_archive(S):
		arch = {}; n = 0
		for entry in S.split("\n"):
			data = entry.split(", ")
			if not data[1] in arch.keys():
				arch[data[1]] = []
			arch[data[1]].append( 
				[n, data[2], data[0].split(".")[1], data[1]]
			)
			n += 1
		return arch
	def rename_archive(S):
		new = []
		for city,value in enumerate(S):
			for entry in value:
				print(entry)
				new.append(
					"".join([entry[3],entry[0],entry[2]])
				)
		return ("\n".join(new))
	archive = compile_archive(A)
	renamed_list = rename_archive(archive)
	return renamed_list

if __name__ == "__main__":
	def test(value, expect):
		test = solution(value)
		if test != expect:
			print("MISTAKE %s != %s (value was %s)"%(test, expect, value))
		else:
			print("CORRECT %s == %s (value was %s)"%(test, expect, value))
	print("TESTS:")
	test("photo.jpg, Warsaw, 2013-09-05 14:08:15\n \
		john.png, London, 2015-06-20 15:13:22\n \
		myFriends.png, Warsaw, 2013-09-05 14:07:13\n \
		Eiffel.jpg, Paris, 2015-07-23 08:03:02\n \
		pisatower.jpg, Paris, 2015-07-22 23:59:59\n \
		BOB.jpg, London, 2015-08-05 00:02:03\n \
		notredame.png, Paris, 2015-09-01 12:00:00\n \
		me.jpg, Warsaw, 2013-09-06 15:40:22\n \
		a.png, Warsaw, 2016-02-13 13:33:50\n \
		b.jpg, Warsaw, 2016-01-02 15:12:22\n \
		c.jpg, Warsaw, 2016-01-02 14:34:30\n \
		d.jpg, Warsaw, 2016-01-02 15:15:01\n \
		e.png, Warsaw, 2016-01-02 09:49:09\n \
		f.png, Warsaw, 2016-01-02 10:55:32\n \
		g.jpg, Warsaw, 2016-02-29 22:13:11",0)
	#test(2,0)
	#test(3,0)
	