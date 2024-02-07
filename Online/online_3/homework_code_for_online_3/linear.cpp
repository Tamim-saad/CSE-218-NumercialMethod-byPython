import numpy as np
import matplotlib.pyplot as plt

def exp(x,a,b):
  return a0+a1*x

def exp0(x,a):
  return a*x

p = []
q = []
r = []
n=0
flag= False

data= np.loadtxt('input.txt')
for row in data:
  n=n+1
  a=float(row[0])
  b=float(row[1])
  p.append(a)
  q.append(b)
  if(a==0 and b==0):
    flag=True

x = np.array(p)
y = np.array(q)
newx=[]
newy=[]

print(len(x), " --- ", len(y), "  ")

# print("------------- ",n)


# for i in range(n):
#   print(x[i]," ",y[i]," --- ")


xy_product_sum=0
xsum=0
ysum=0
xsquare_sum=0
ysquare_sum=0
a1=0
a0=0

for i in range(n):
  xsum=xsum+float(x[i])
  ysum=ysum+float(y[i])
  xsquare_sum=xsquare_sum+x[i]**2
  ysquare_sum=ysquare_sum+y[i]**2
  xy_product_sum=xy_product_sum+x[i]*y[i]


# def determine():
a1=(n*xy_product_sum-xsum*ysum)/(n*xsquare_sum-xsum**2)
a0=(xsquare_sum*ysum-xsum*xy_product_sum)/(n*xsquare_sum-xsum**2)
if(flag==True):
  E=xy_product_sum/xsquare_sum
  Y = []
  X = np.linspace(x[0], x[len(x) - 1] )
  Y = exp0(X, E)
  # i=0
  # while (i < n):
  #   newy.append(E * x[i])
  #   i += 1
else:
  Y = []
  X = np.linspace(x[0], x[len(x) - 1] + 5)
  Y = exp(X, a0, a1)




plt.close('all')
plt.scatter(x,y,color='green')

plt.plot(X,Y, label='fitting')

plt.legend(loc='upper right')
plt.xlabel('Concentration of Oxygen')
plt.ylabel('Time')
plt.grid()
plt.show()
