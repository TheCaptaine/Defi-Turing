resultat = 0
for i in range(1, 10000000):
	I, II = str(i), ''
	for k in range(len(I)):
		II += I[-k-1]
	if I == II:
		bI, bII = bin(i)[2:], ''
		for k in range(len(bI)):
			bII += bI[-k-1]
		if bI == bII:
			resultat += i
print(resultat)