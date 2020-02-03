from math import sqrt

def nombreP(n):
     for j in range(2, int(sqrt(n))+1):
             if n%j == 0:
                     return 0
     return 1

def circulaire(p, q):
	Nb = 0
	for k in range(p, q+1):
		if nombreP(k) == True:
			compteur = 0
			ki = k
			for possibilite in range(len(str(k))):
				ron = str(ki)[-1]
				for indice in range(len(str(k))-1):
					ron += str(ki)[indice]
				ki = int(ron)
				if nombreP(ki) == True:
					compteur += 1
				else:
					break
			if compteur == len(str(k)):
				Nb += 1
	print(Nb)
	return

circulaire(2, 100000)