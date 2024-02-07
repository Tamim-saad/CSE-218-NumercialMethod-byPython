import numpy as np
import matplotlib.pyplot as plt

p = []
q = []
r = []
n=0
flag= False

def exp(x,a,b):
  return a*2.718281828**(b*x)

data= np.loadtxt('input.txt')
for row in data:
  n=n+1
  a=float(row[0])
  b=float(row[1])
  p.append(a)
  q.append(np.log10(b)/np.log10(2.718281828))
  r.append(b)

x = np.array(p)
y = np.array(q)
y2=np.array(r)

# for i in range(n):
#   print(x[i]," ",y[i]," --- ")


xy_product_sum=0
xsum=0
ysum=0
xsquare_sum=0
ysquare_sum=0


for i in range(n):
  xsum=xsum+float(x[i])
  ysum=ysum+float(y[i])
  xsquare_sum=xsquare_sum+x[i]**2
  ysquare_sum=ysquare_sum+y[i]**2
  xy_product_sum=xy_product_sum+x[i]*y[i]

a1=(n*xy_product_sum-xsum*ysum)/(n*xsquare_sum-xsum**2)
a0=(xsquare_sum*ysum-xsum*xy_product_sum)/(n*xsquare_sum-xsum**2)

a=2.718281828**a0
b=a1

# i=0
# y=[]
# while(i<n):
#   y.append(a*(2.718281828**(b*x[i])))
#   i+=1

#-------------------------------------------------------------------
X=np.linspace(x[0],x[len(x)-1]+5)
Y=exp(X,a,b)
plt.close('all')

plt.plot(X,Y, label='fitting')
plt.scatter(x,y2,color='red')

plt.legend(loc='upper right')
plt.xlabel('Concentration of Oxygen')
plt.ylabel('Time')
plt.grid()
plt.show()