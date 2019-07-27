def decompose(n):  
	i = 1
	while n > 1: 
		while n%i == 0: 
			n /= i 
		i += 1
	return i
	
print(decompose(2013))