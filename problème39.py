from math import *

s = []

for p in range(1, 150):
	c = 0
	for i in range(1, p):
		for j in range(1, p):
			ij = i + j
			if ij >= p:
				break
			for k in range(1, p):
				ijk = ij + k
				if ijk > p:
					break
				if p == ijk:
					c += 1
	s += [c]
	print(p)
c = 0
for i in s:
	print("{} : {}".format(i, c))
	c += 1
#print("Nombre de solution maximum pour p = {} avec un nombre de solution de {}".format(s.index(max(s)))+1, max(s))