def syracuse(n):
	i = 1
	while n != 1:
		if n%2 == 0:
			n /= 2
		else:
			n = n * 3 + 1
		i += 1
	return i

dictionaire = {}

for k in range(1, 1500000):
	dictionaire[k] = syracuse(k)

print(max(dictionaire, key=dictionaire.get))