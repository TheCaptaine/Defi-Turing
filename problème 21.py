liste1, liste2 = [], []
for i in range(1, 2014):
	a, I = 0, str(i)
	for j in range(len(I)):
		if I[j] in I[:j] or I[j] in I[j+1:]:
			a = 1
			break
	if a == 0:
		liste1 += [i]

for i in range(len(liste1)-1):
	liste2 += [liste1[i+1] - liste1[i]]

print(len(liste1)*max(liste2))
		