annulaire_vert, annulaire_bleu, a, b, c, d = [], [], 0, 0, 0, 0

for i in range(1, 2014):
	b += 1
	c += 1
	d += 1
	if a%2 == 0 and b == 2 or a%2 == 1 and b == 12:
		annulaire_vert += [i]
		a += 1
		b = 0
	if d%2 == 0 and c == 2 or d%2 == 1 and c == 10:
		annulaire_bleu += [i]
		d += 1
		c = 0
		
r = 0

for i in annulaire_vert:
	if i in annulaire_bleu:
		r += i

print(r)