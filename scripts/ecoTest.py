def ecoTest(fun):
	print(fun(10))
		
def test(n):
	return n+n*2-5

if __name__ == "__main__":
	ecoTest(test)
	