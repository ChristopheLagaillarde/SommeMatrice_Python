try:
    n = int(input("Saisir la tailles des 2 Matrice 2D"))
    M1 = [[int(input("Matrice 1 =")) for x in range(n)] for y in range(n)]
    M2 = [[int(input("Matrice 2 =")) for x in range(n)] for y in range(n)]
    M3 = [[0 for i in range(n)] for j in range(n)]

    for i in range(len(M3)):
        for j in range(len(M3)):
            M3[i][j] = M1[i][j] + M2[i][j]

    print("Resultat:\n")
    print("M1 =", M1)
    print("M2 =", M2)
    print("M3 =", M3)

except ValueError:
    print("Saisie non valide")
