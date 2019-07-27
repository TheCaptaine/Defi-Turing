def palindrome(n):
	l = ""
	strn = str(n)
	if n == int(''.join([strn[-k] for k in range(1, len(strn) + 1)])):
		return 1

nb = []

for i in range(1000, 10000):
	for j in range(100, 1000):
		r = i * j
		if palindrome(r) == 1:
			nb.append(r)
print(max(nb))