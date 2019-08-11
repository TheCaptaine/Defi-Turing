liste, n = [], 1000
for a in range(2, n+1):
	for b in range(2, n+1):
		c = a**b
		if c not in liste:
			liste += [c]
print(len(liste))