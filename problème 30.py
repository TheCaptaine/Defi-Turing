r = 0
for i in range(2, 1000000):
	I, a = str(i), 0
	for k in range(len(I)):
		a += int(I[k])**5
	if a == i:
		r += i
print(r)