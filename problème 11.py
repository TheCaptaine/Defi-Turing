def miroir(n):
	m = str(n)
	r = ''
	for i in range(len(m)):
		r += m[-i-1]
	return int(r)

for j in range(int(10e6)):
	if miroir(j) == 4 * j:
		last_nb = j
print(last_nb)
