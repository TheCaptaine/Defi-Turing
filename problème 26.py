for i in range(111111111, 1000000000):
	a = 0
	I = str(i)
	if '0' in I or '1' not in I or '2' not in I or '3' not in I or '4' not in I or '5' not in I or '6' not in I or '7' not in I or '8' not in I or '9' not in I:
		pass
	else:
		for k in range(1, 10):
			if int(I[:k])%(k) != 0:
				a = 1
				break
		if a == 0:
			print(i)
			break

