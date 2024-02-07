import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return -((6.73 * x + 6.725 * 10 ** (-8) + 7.26 * 0.0005 * 10 ** (-4)) / (
            3.62 * x * 10 ** (-12) + 0.0005 * x * 3.908 * 10 ** (-8)))


# --------------------------------------------
def trapezoidal(a, b, n):
    h = (b - a) / n
    s = f(a) + f(b)

    i = 1
    while i < n:
        s += 2 * f(a + i * h)
        i += 1
    return ((h / 2) * s)


# --------------------------------------------
def simpson1_3(a, b, n):
    n = 2 * n
    h = (b - a) / n

    ans = 0
    i = 0
    while i < n:
        ans += (h / 3) * (f(a + i * h) + f(a + (i + 2) * h) + 4 * f((a + i * h + a + (i + 2) * h) / 2))
        i = i + 2
    return ans


# --------------------------------------------

a = 0.75 * 1.22 * 10 ** (-4)
b = 0.25 * 1.22 * 10 ** (-4)

segment = int(input("Enter number of segments : "))

# -----------------------trapezoidal driver code---------------------

i = 1
print("\n---iteration---  ", "---Value---  ", " ---Relative Error in trapezoid---")
while i <= segment:
    sum_by_trapezoidal = trapezoidal(a, b, i)
    if i == 1:
        prev_sum_by_trapezoidal = sum_by_trapezoidal
        print('\n', i, "        ", sum_by_trapezoidal, "     ", ".......")
        i = i + 1
        continue

    aprox_error = abs(sum_by_trapezoidal - prev_sum_by_trapezoidal) / sum_by_trapezoidal * 100
    print('\n', i, "        ", sum_by_trapezoidal, "     ", aprox_error, " %")

    prev_sum_by_trapezoidal = sum_by_trapezoidal
    i = i + 1

print("\033[1m" + "\nArea By Trapezoid: " + "\033[0m")
print(sum_by_trapezoidal, '\n')

# -----------------------simpson driver code--------------------------

i = 1
print("---iteration---  ", "---Value---  ", " ---Relative Error in simpson---")
while i <= segment:
    sum_by_simpson = simpson1_3(a, b, i)
    if i == 1:
        prev_sum_by_simpson = sum_by_simpson
        print('\n', i, "        ", sum_by_simpson, "     ", ".......")
        i = i + 1
        continue
    aprox_error = abs(sum_by_simpson - prev_sum_by_simpson) / sum_by_simpson * 100
    print('\n', i, "        ", sum_by_simpson, "     ", aprox_error, " %")

    prev_sum_by_simpson = sum_by_simpson
    i = i + 1

print("\033[1m" + "\nArea By Simpson: " + "\033[0m")
print(sum_by_simpson, '\n')

# --------------------graph---------------------------

x = np.array(
    [1.22 * 10 ** (-4), 1.20 * 10 ** (-4), 1.0 * 10 ** (-4), 0.8 * 10 ** (-4), 0.6 * 10 ** (-4), 0.4 * 10 ** (-4),
     0.2 * 10 ** (-4)])
p = []
p.append(0)
size = x.size
i = 1
while i < size:
    a = float(x[0])
    b = float(x[i])
    p.append(simpson1_3(a, b, 10))
    i += 1
y = np.array(p)

plt.close('all')
plt.plot(x, y, label='f(time)')
plt.scatter(x, y, color='red')
plt.legend(loc='upper right')
plt.xlabel('Concentration of Oxygen,x(mole/cm^3)')
plt.ylabel('Time,T(sec)')
plt.grid()
plt.show()
