"""
Task 2

"""
def solution(A, D):
	def get_month(d):
		return int(d.split("-")[1])-1
	year = [[],[],[],[],[],[],[],[],[],[],[],[]]
	for i,t in enumerate(A):
		m = get_month(D[i])
		year[m].append(t)
	for m in year:
		p = [i for i in m if i < 0]
		if len(p) < 3 or sum(p) > -100:
			m.append(-5)
	print(year)
	return (sum(map(sum, year)))

if __name__ == "__main__":
	def test(value1, value2, expect):
		test = solution(value1, value2)
		if test != expect:
			print("MISTAKE %s != %s (value was %s | %s)"%(test, expect, value1, value2))
		else:
			print("CORRECT %s == %s (value was %s | %s)"%(test, expect, value1, value2))
	print("TESTS:")
	test([10,100,100], ["2020-12-23","2020-12-31","2020-12-12"],150)
	test([10,100,100, -99, -100], ["2020-12-23","2020-12-31","2020-12-12","2020-04-12","2020-5-12"],-49)
	test([10,100,100, -20, -20, -60], ["2020-12-23","2020-12-31","2020-12-12","2020-04-12","2020-4-12","2020-4-12"],55)

	