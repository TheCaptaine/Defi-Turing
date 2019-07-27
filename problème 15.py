import itertools
point_grille = [n[0]*n[1]*n[2] + n[3]*n[4]*n[5] + n[6]*n[7]*n[8] + n[0]*n[3]*n[6] + n[1]*n[4]*n[7] + n[2]*n[5]*n[8] for n in list(itertools.permutations([1, 2, 3, 4, 5, 6, 7, 8, 9]))]
print(max(point_grille)*min(point_grille))