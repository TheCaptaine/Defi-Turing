def d(n):
	a = 0
	for i in range(1, n):
		if n%i == 0:
			a += i
			if a > n: break
	return a

liste, r = [], 0

for n in range(1, 2014):
	if d(n) > n:
		liste += [n]

for i in range(1, 2014):
	c = 0
	for n in liste:
		m = i - n
		if m < 0:
			r += i
			break
		if m not in liste: c += 1
		else: break
		if c == len(liste): r += i

print(r)