from math import factorial
a = 1
for i in range(3, 100000):
	I, b = str(i), 0
	for k in range(len(I)):
		b += factorial(int(I[k]))
	if b == i:
		a *= i
print(a)

