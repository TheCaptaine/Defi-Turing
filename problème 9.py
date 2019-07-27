liste = []
for y in range(3600):
    for x in range(y):
        z = (x**2 + y**2)**(1/2)
        if x + y + z == 3600:
            liste += [x * y * z]
print(max(liste))