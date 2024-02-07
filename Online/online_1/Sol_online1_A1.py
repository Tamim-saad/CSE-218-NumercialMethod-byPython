import matplotlib.pyplot as plt
import numpy as np
e=2.718281828

def f(x):
    ans=2*70*e**(-1.5*x)+2*25*e**(-0.075*x)-95
    #ans=2*2.718281828**(-0.5*x)*np.cos(3*x)-1
    return ans


plt.close('all')
x = np.linspace(-10, 10, 1000)
y = f(x)
plt.plot(x, y)
plt.legend(loc='lower right')
plt.xlabel('t')
plt.ylabel('c')
plt.grid()
plt.show()
#-------------------------bisection_method-----------------------------------------
mid=0
error=1
left=0
right=0.8
right_f=f(right)


i=0;
while error>0.0001:
    mid=(left+right)/2
    mid_f=f(mid)

    if mid_f*right_f<0:
        left=mid
    else:
        right=mid
    i=i+1
    if i==1:
        past_mid=mid
        continue

    error =( abs(mid - past_mid) / mid) * 100
    past_mid = mid

print("Online A1: ",mid)