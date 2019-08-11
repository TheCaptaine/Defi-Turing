from math import sqrt

def estpremier(n):
	if n < 7:
		if n in (2,3,5):
			return 1
		else:
			return 0
	if n & 1 == 0:
		return 0
	k = 3
	r = sqrt(n)
	while k <= r:
		if n % k == 0:
			return 0
		k += 2
	return 1

f = lambda n, a, b: n**2 + n * a + b

N, A, B = [], [], []

for a in range(-1499, 1500):
	for b in range(-1499, 1500):
		n = 0
		while estpremier(f(n, a, b)) == 1:
			n += 1
		N += [n]
		A += [a]
		B += [b]

l = N.index(max(N))
print(A[l]*B[l])