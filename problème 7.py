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

i = 0
j = 0

while j < 23456:
	if estpremier(i) == 1:
		j += 1
	i += 1
	
print(i - 1)