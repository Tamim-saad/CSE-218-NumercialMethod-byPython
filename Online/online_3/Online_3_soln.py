import numpy as np
import matplotlib.pyplot as plt

def exp(x,a,b):
  # return a*2.718281828**(b*x)
  #   return  sol0*+sol2*(x**2)
       return 1/((b+x*x)/(a*x*x))
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
fst = []
lst=[]
n = 0

data = np.loadtxt('Online_3_input_(poly_order=2).txt')
for r in data:
    n = n + 1
    fst.append((float(r[0])))
    lst.append((float(r[1])))
    p.append(1/float(r[0]))
    q.append(1/float(r[1]))

outx=np.array(fst)
outy=np.array(lst)

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
A=1/sol[0]
B=sol[2]/sol[0]

print("a: ",A,"b: ",B)

# -----------------------------------------------------

X=np.linspace(fst[0],lst[len(lst)-1],100)
# Y=[]
# i = 0
# while (i < 100):
#     sum = 0
#
#     j = 0
#     while (j < len(sol)):
#         if(j!=1): sum += sol[j] * (X[i] ** j)
#         j += 1
#     Y.append(sum)
#     i += 1

extrax=[]
extray=[]
extrax.append(2)
extrax.append(4.5)
extray.append(exp(2,A,B))
extray.append(exp(4.5,A,B))
ex_x=np.array((extrax))
ex_y=np.array(extray)



# X=np.linspace(x[0]-5,x[len(x)-1]+5)
Y=exp(X,A,B)
# ---------------------------------------------------------------------------
plt.close('all')
# plt.plot(x, y, label='given')
# plt.scatter(X, Y, color='green')

plt.plot(X, Y, label='fitting')
plt.scatter(outx, outy, color='red')
plt.scatter(ex_x, ex_y, color='black')

plt.legend(loc='lower right')
plt.xlabel('value of x...')
plt.ylabel('value of y...')
plt.grid()
plt.show()