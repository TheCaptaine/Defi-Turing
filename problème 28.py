n = 2013
nb_impair = [i for i in range(n+1) if i%2 == 1]
spirale = []
for i in range(n):
	passage = []
	for k in range(n):
		passage.append(0)
	spirale += [passage]
ligne, colonne, a = int(n/2), int(n/2), 9
for nb in nb_impair:
	if nb == 1:
		spirale[ligne][colonne] = 1
	elif nb == 3:
		spirale[ligne][colonne+1] = 2
		spirale[ligne+1][colonne+1] = 3
		spirale[ligne+1][colonne] = 4
		spirale[ligne+1][colonne-1] = 5
		spirale[ligne][colonne-1] = 6
		spirale[ligne-1][colonne-1] = 7
		spirale[ligne-1][colonne] = 8
		spirale[ligne-1][colonne+1] = 9
		ligne, colonne = ligne-1, colonne+1
	else:
		for k in range(4):
			if k == 0:
				colonne += 1
			elif k == 1:
				ligne -= 1
				colonne -= 1
			elif k == 2:
				colonne += 1
				ligne -= 1
			elif k == 3:
				ligne += 1
				colonne += 1
			for i in range(nb-1):
				a += 1
				if k == 0:
					spirale[ligne][colonne] = a
					ligne += 1
				elif k == 1:
					spirale[ligne][colonne] = a
					colonne -= 1
				elif k == 2:
					spirale[ligne][colonne] = a
					ligne -= 1
				elif k == 3:
					spirale[ligne][colonne] = a
					colonne += 1
		colonne -= 1

print(sum([spirale[i][i] for i in range(n)]) + sum([spirale[n-1-i][i] for i in range(n)]) - 1)





