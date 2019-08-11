liste = []
for i in range(100000, 1000000):
	I, II, a = str(i), str(i*8), 0
	if len(II) == 6:
		for k in range(6):
			if I[k] not in II or I.count(I[k]) != II.count(I[k]):
				a = 1
				break
		if a == 0:	
			liste += [i]

print(sum(liste))
