def miroir(n):
	m = str(n)
	r = ''
	for i in range(len(m)):
		r += m[-i-1]
	return int(r)

i = 836

while True:
	i += 1
	I = i**2
	if I == miroir(I) and len(str(I))%2 == 0:
		print(I)
		break