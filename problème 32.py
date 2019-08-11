liste = []
for i in range(2, 10000):
	I, c = str(i), 0
	for k in range(len(I)):
		if '0' in I or I[k] in I[:k] or I[k] in I[k+1:]:
			c = 1
			break
	if c == 0:
		for j in range(1, i):
			a = i%j
			if a == 0:
				J, c = str(j), 0
				for k in range(len(J)):
					if '0' in J or J[k] in J[:k] or I[k] in I[k+1:] or J[k] in I:
						c = 1
						break
				if c == 0:
					a = int(i/j)
					A = str(a)
					for l in range(len(A)):
						if '0' in A or A[l] in A[:l] or A[l] in A[l+1:] or A[l] in J or A[l] in I:
							c = 1
							break
					if c == 0:
						for p in range(1, 10):
							P = str(p)
							if P not in A and P not in J and P not in I:
								c = 1
								break
						if c == 0 and i not in liste:
							liste += [i]
							print("{} * {} = {} (a * j = i)".format(a, j, i))
print(sum(liste))


						
							
