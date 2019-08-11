liste = []

for i in range(1, 100000):
	a = 0
	for k in range(1, i):
		if i%k == 0:
			a += k
	liste += [(i, a)]

print(sum([i[0] for i in liste if (i[1], i[0]) in liste and i[0] != i[1]]))