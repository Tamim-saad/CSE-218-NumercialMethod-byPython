import numpy as np
import matplotlib.pyplot as plt

# def exp(x,a,b):
#   return a*2.718281828**(b*x)

def Gaussian(A, B, piv):
    n = int((np.size(A)) ** .5)
    for i in range(0, n - 1):
        if piv == True:
            max = abs(A[i, i])
            row = i

            for r in range(i + 1, n):
                if abs(A[r, i]) > max:
                    max = abs(A[r, i])
                    row = r
            if row != i:
                for swap in range(0, n):
                    tem = A[i, swap]
                    A[i, swap] = A[row, swap]
                    A[row, swap] = tem

                tem2 = B[i]
                B[i] = B[row]
                B[row] = tem2

        for j in range(i, n - 1):
            multi = A[j + 1, i] / A[i, i]
            for k in range(i, n):
                A[j + 1, k] -= A[i, k] * multi
            B[j + 1] -= B[i] * multi
    sol = [0] * n

    sol[n - 1] = B[n - 1] / A[n - 1, n - 1]

    i = n - 2
    while i >= 0:
        tem = B[i]
        for j in range(i, n - 1):
            B[i] = B[i] - A[i, j + 1] * sol[j + 1]
        sol[i] = B[i] / A[i, i]
        i = i - 1

    sol = np.array(sol)
    sol = np.reshape(sol, (n, 1))
    return sol


# --------------------------------------------------------------------------------

p = []
q = []
r = []
n = 0

data = np.loadtxt('input.txt')
for r in data:
    n = n + 1
    p.append(float(r[0]))
    q.append(float(r[1]))

x = np.array(p)
y = np.array(q)

# -------------------------------------------------------
newy = []
x_power_array = []
xy_product_array = []
a1 = 0
a0 = 0
m = int(input("Enter the polynomial order:"))
Arr = []
Arr.append(n)
x_power_array.append(n)

# print(len(x), " --- ", len(y), "  ")
# print("------------- ",n)

# ------------------------------------------------------------
i = 1
while (i <= 2 * m):
    sum = 0
    for j in range(n):
        sum += x[j] ** i
    x_power_array.append(sum)
    i += 1

i = 0
while (i <= m):
    sum = 0
    for j in range(n):
        sum += (x[j] ** i) * y[j]
    xy_product_array.append(sum)
    i += 1

i = 0
while (i <= m):
    j = 0;
    while (j <= m):
        if (i == 0 and j == 0):
            j = j + 1
            continue
        Arr.append(x_power_array[i + j])
        j += 1
    i = i + 1

A = np.matrix(Arr)
A = A.reshape(m + 1, m + 1)
# print(A)

sol = Gaussian(A, xy_product_array, True)
# print(" --- ",sol)

# -----------------------------------------------------

X=np.linspace(x[0]-5,x[len(x)-1]+5,100)
Y=[]
i = 0
while (i < 100):
    sum = 0

    j = 0
    while (j < len(sol)):
        sum += sol[j] * (X[i] ** j)
        j += 1
    Y.append(sum)
    i += 1

# X=np.linspace(x[0]-5,x[len(x)-1]+5)
# Y=exp(X,a,b)
# ---------------------------------------------------------------------------
plt.close('all')
# plt.plot(x, y, label='given')
# plt.scatter(X, Y, color='green')

plt.plot(X, Y, label='fitting')
plt.scatter(x, y, color='red')

plt.legend(loc='upper right')
plt.xlabel('Concentration of Oxygen')
plt.ylabel('Time')
plt.grid()
plt.show()