hydres, a = [4], 1

while hydres != []:
	if hydres[-1] == 2:
		a += a + 1
		del hydres[-1]
	else:
		hydres[-1] -= 1
		hydres += [hydres[-1]] * a
	a += 1

print(a - 1)