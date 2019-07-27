def draw_carre_in_rectangle_(n, rectangle):
	i, dictionnaire = 0, []
	for ligne in range(len(rectangle)):
		for colonne in range(len(rectangle[0])):
			for k in range(4):
				if k == 0:
					try:
						matricule = '{}:{} {}:{} {}:{}'.format(ligne, colonne, ligne + n, colonne, ligne, colonne + n)
						if matricule not in dictionnaire:
							rectangle[ligne][colonne] = 1
							rectangle[ligne + n][colonne] = 1
							rectangle[ligne][colonne + n] = 1
							dictionnaire += [matricule]
							i += 1	
					except IndexError:
						pass
				elif k == 1 and ligne - n >= 0:
					try:
						matricule = '{}:{} {}:{} {}:{}'.format(ligne - n, colonne, ligne, colonne, ligne - n, colonne + n)
						if matricule not in dictionnaire:
							rectangle[ligne][colonne] = 1
							rectangle[ligne - n][colonne] = 1
							rectangle[ligne][colonne + n] = 1
							dictionnaire += [matricule]
							i += 1	
					except IndexError:
						pass
				elif k == 2 and colonne - n >= 0:
					try:
						matricule = '{}:{} {}:{} {}:{}'.format(ligne, colonne - n, ligne + n, colonne - n, ligne, colonne)
						if matricule not in dictionnaire:
							rectangle[ligne][colonne] = 1
							rectangle[ligne + n][colonne] = 1
							rectangle[ligne][colonne - n] = 1
							dictionnaire += [matricule]
							i += 1	
					except IndexError:
						pass
				elif k == 3 and ligne - n >= 0 and colonne - n >= 0:
					try:
						matricule = '{}:{} {}:{} {}:{}'.format(ligne - n, colonne - n, ligne, colonne - n, ligne - n, colonne)
						if matricule not in dictionnaire:
							rectangle[ligne][colonne] = 1
							rectangle[ligne - n][colonne] = 1
							rectangle[ligne][colonne - n] = 1
							dictionnaire += [matricule]
							i += 1	
					except IndexError:
						pass
	return i

colonne, ligne, n, i, carre = 20, 1, 0, 0, 0

while carre + colonne * ligne < 6400:
	f, n, carre, rectangle = 1, 0, 0, [[0 for i in range(colonne)]]*ligne
	while f != 0:
		n += 1
		f = draw_carre_in_rectangle_(n, rectangle)
		carre += f
	if carre + colonne * ligne > 6400:
		colonne += 1
		ligne = 0
	ligne += 1

ligne -= 1
print("Nbs de petits carré pour un rectangle de diamètre {} * {} : {}\nAire du rectangle : {}\n".format(colonne, ligne, carre + colonne * ligne, colonne * ligne))



