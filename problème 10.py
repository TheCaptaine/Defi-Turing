from math import sqrt

def nombre_premier_inf_n_(n):
	r = 0
	for i in range(2, n):
		a = 0
		if i%2 == 0:
			a = 1
		else:
			for j in range(2, int(sqrt(i))+1):
				if i%j == 0:
					a = 1
		if a == 0:
			r += i
	return r + 2

print(nombre_premier_inf_n_(10000000))