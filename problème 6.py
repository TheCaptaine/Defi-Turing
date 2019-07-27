def factoriel(n, i = 1):
	for k in range(1, n+1):
		i *= k
	return i
	
nb = str(factoriel(2013))
print(sum([int(nb[k]) for k in range(len(nb))]))