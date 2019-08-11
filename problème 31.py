r, R = 0, 1000
for a in range(0, R+1, 500):
	R = 1000 - a
	for b in range(0, R+1, 200):
		R = 1000 - a - b
		for c in range(0, R+1, 100):
			R = 1000 - a - b - c
			for d in range(0, R+1, 50):
				R = 1000 - a - b - c - d
				for e in range(0, R+1, 20):
					R = 1000 - a - b - c - d - e
					for f in range(0, R+1, 10):
						R = 1000 - a - b - c - d - e - f
						for g in range(0, R+1, 5):
							h = 1000 - a - b - c - d - e - f - g
							if h == 0:
								r += 1
print(r)