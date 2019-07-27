def fibonacci(n):
	a, b = 1, 1
	if n == 0:
		return 0
	for n in range(n - 1):
		a, b = b, a + b
	return a

nb = 0	
i = 0
f = 0

while f < 4e6:
	if f%2 == 1:
		nb += f
	i += 1	
	f = fibonacci(i)
print(nb)