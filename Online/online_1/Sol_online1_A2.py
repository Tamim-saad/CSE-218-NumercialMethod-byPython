import matplotlib.pyplot as plt
import numpy as np
e=2.718281828

def f(x):
    #ans=2*70*e**(-1.5*x)+2*25*e**(-0.075*x)-95
    ans=2*2.718281828**(-0.5*x)*np.cos(3*x)-1
    return ans


plt.close('all')
x = np.linspace(-10, 10, 1000)
y = f(x)
plt.plot(x, y,label='f(x)')
plt.legend(loc='lower right')
plt.xlabel('t')
plt.ylabel('c')
plt.grid()
plt.show()
#------------------------------------------------------------------

x2=0.25
x1=0.35
error=1

i=0;
while error>0.0001:
    xtem=x2
    x2=x2-f(x2)*((x2-x1)/(f(x2)-f(x1)))
    x1=xtem
    error =( abs(x2 - xtem) / xtem) * 100
    i=i+1
    print("estimated root after iteration",i,": ",x2)

print("online A2: ",x2)

