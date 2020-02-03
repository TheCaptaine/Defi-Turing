def Conway(n):
	u = '2'
	for k in range(n-1):
		stock, compteur = "", 1
		for indice in range(len(u)):
			try:
				if u[indice] == u[indice+1]:
					compteur += 1
				else:
					stock += str(compteur) + u[indice]
					compteur = 1
			except IndexError:
				stock += str(compteur) + u[indice]
		u = stock
	return u

ConwayT50, a = str(Conway(50)), 0

for i in range(len(ConwayT50)):
	if ConwayT50[i] == '1':
		a += 1
print(a)