"""
Given a year, return the century it is in.
The first century spans from the year 1 up to and including the year 100, the second - from the year 101 up to and including the year 200, etc.

Example

    For year = 1905, the output should be
    centuryFromYear(year) = 20;
    For year = 1700, the output should be
    centuryFromYear(year) = 17.

Input/Output

    [execution time limit] 4 seconds (py)

    [input] integer year

    A positive integer, designating the year.

    Guaranteed constraints:
    1 ≤ year ≤ 2005.

    [output] integer

    The number of the century the year is in.

[Python 2] Syntax Tips

# Prints help message to the console
# Returns a string
def helloWorld(name):
    print "This prints to the console when you Run Tests"
    return "Hello, " + name
"""
def centuryFromYear(year):
	if (year % 100 != 0):
		return (int (year / 100) + 1)
	return (int (year / 100))

if __name__ == "__main__":
	def test(value, expect):
		test = centuryFromYear(value)
		if test != expect:
			print("MISTAKE %d != %d (value was %d)"%(test, expect, value))
		else:
			print("MISTAKE %d == %d (value was %d)"%(test, expect, value))
	print("TESTS:")
	test(1905, 20)
	test(1700, 17)
	test(1701, 18)
