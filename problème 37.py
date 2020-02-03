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

a, j, r, i = 0, 0, 0, 10
while j != 11:
	I, b = str(i), 0
	for k in range(len(I)):
		if estpremier(int(I[:k+1])) == 0:
			b = 1
			break
	if b == 0:
		for k in range(len(I)):
			if estpremier(int(I[-k-1:])) == 0:
				b = 1
				break
		if b == 0:
			j += 1
			r += i
	i += 1
print(r)

