def fibonacci(n):
	a, b = 1, 1
	if n == 0:
		return 0
	for n in range(n - 1):
		a, b = b, a + b
	return a

n = 1

while len(str(fibonacci(n))) < 2013:
	n += 1
	
print(n)