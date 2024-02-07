import numpy as np


def GaussianElimination(A, B, pivot, showall):
    length = len(B)
    flag = 0
    flag1 = False
    for j in range(0, length - 1):
        if pivot:
            max = abs(A[j][j])
            for m in range(j + 1, length):
                if abs(A[m][j]) > max:
                    max = abs(A[m][j])
                    p = m
                    flag1 = True
                else:
                    p = j
            if flag1:
                flag += 1
            flag1 = False
            A[[j, p]] = A[[p, j]]
            B[[j, p]] = B[[p, j]]
        for i in range(j + 1, length):
            if A[i, j] == 0: continue
            f = A[i, j] / A[j, j]
            A[i, j:length] = A[i, j:length] - f * A[j, j:length]
            B[i] = B[i] - B[j] * f
            if showall:
                print("Matrix of A:\n", A)
                print("Matrix of B:\n", B)

    x = np.zeros(n, dtype=float)
    for i in range(n - 1, -1, -1):
        x[i] += B[i]
        for j in range(i + 1, n):
            x[i] -= A[i, j] * x[j]
        x[i] /= A[i, i]
    determinant = 1
    if showall:
        print("\nDeterminant of co-efficient matrix of A after GaussianElimination:")
        # print(np.linalg.det(A))
        for i in range(0, length):
            for j in range(0, length):
                if i == j:
                    determinant *= A[i][j]
        if flag % 2 != 0:
            print("\n", -determinant)
        else:
            print(determinant)

    print("\nSolutions of X:")
    for i in range(n):
        print("%.4f" % (x[i]))


if __name__ == "__main__":
    n = int(input())
    A = []
    # 1st appending numbers for number of columns times
    # Then appending this 1-D list into the empty row list
    for i in range(n):
        a = []
        for j in range(n):
            a.append(float(str(input())))
        A.append(a)

    A = np.array(A)
    print(A)
    b = []
    for i in range(n):
        b.append([float(input())])

    B = np.array(b)
    print(B)
    GaussianElimination(A, B, False, True)
