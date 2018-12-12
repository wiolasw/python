import numpy as np

A = np.random.random_integers(8, size=(8,8))
B = np.random.random_integers(8, size=(8,8))
print(A)
print(B)

wiersze_A = len(A)
kolumny_A = len(A[0])
wiersze_B = len(B)
kolumny_B = len(B[0])

C = np.zeros((8, 8))
print(C)

for i in range(wiersze_A):
    for j in range(kolumny_B):
        for k in range(kolumny_A):
            C[i][j] += A[i][k] * B[k][j]
print(C)


D = np.matmul(A,B)
print(D)