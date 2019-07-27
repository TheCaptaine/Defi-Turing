# THREE
THREE = []
for i in range(0, 100000):
	a = 0
	if i%9 == 0:
		I = str(i)
		I = '0'*(5 - len(I)) + I
		if I[-1] == I[-2]:
			for k in range(3):
				if I[k] in I[k+1:-1]:
					a = 1
					break
			if a == 0:
				THREE += [I]

# NINE
NINE = []
for i in range(0, 10000):
	if i%3 == 0:
		I = str(i)
		I = '0'*(4 - len(I)) + I
		if I[0] == I[2] and I[1] != I[0] and I[1] != I[3] and I[0]!= I[3]:
			NINE += [I]

# TROIS
TROIS = []
for i in range(0, 100000):
	a = 0
	if i%3 == 0:
		I = str(i)
		I = '0'*(5 - len(I)) + I
		for k in range(4):
			if I[k] in I[k+1:]:
				a = 1
				break
		if a == 0:
			TROIS += [(K[0], M, K[1]) for K in [(J, I) for J in THREE if I[0] == J[0] and I[1] == J[2] and J[1] not in I[-3:] and J[3] not in I[-3:]] for M in NINE if K[0][3] == M[3] and K[1][3] == M[1] and M[0] not in K[1] and M[0] != K[0][1]]

# NEUF
NEUF = []
for i in range(0, 10000):
	a = 0
	if i%9 == 0:
		I = str(i)
		I = '0'*(4 - len(I)) + I
		for k in range(3):
			if I[k] in I[k+1:]:
				a = 1
				break
		if a == 0:
			NEUF += [(int(K[0]), int(K[1]), int(K[2]), i) for K in TROIS if I[0] == K[1][0] and I[1] == K[1][3] and I[2] not in K[0] and I[2] != K[0][1] and I[3] not in K[0] and I[3] != K[0][1]]

# THREE x NINE = TROIS x NEUF
for k in ['{} x {} = {} x {} = {}'.format(i[0], i[1], i[2], i[3], i[0] * i[1]) for i in NEUF if i[0] * i[1] == i[2] * i[3]]: print(k)