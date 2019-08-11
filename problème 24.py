import itertools
a = 0
for n in list(itertools.permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])):
	a += 1
	if a == 2000000:
		for i in range(len(n)):
			print(n[i], end = '')