a = 0
for annee in range(2001, 10000):
	n = annee%19
	u = annee%100
	c = int((annee - u)/100)
	t = c%4
	s = int((c - t)/4)
	C = c+8
	p = int((C - C%25)/25)
	P = c-p+1
	q = int((P - P%3)/3)
	e = (19*n+c-s-q+15)%30
	d = u%4
	b = int((u - d)/4)
	l = (2*t+2*b-e-d+32)%7
	ll = n+11*e+22*l
	L = ll%451
	h = int((ll - L)/451)
	E = e+l-7*h+114
	j = E%31
	m = int((E - j)/31)
	if m == 4:
		a += 1
print(a)
