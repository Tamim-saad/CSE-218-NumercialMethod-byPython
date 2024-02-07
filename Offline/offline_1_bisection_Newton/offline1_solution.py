def f(x):
    ans=x**3-0.18*x*x+.0004752
    return ans

def fprime(x):
    ans=3*x*x-2*0.18*x
    return ans

#-------------------------bisection_method-----------------------------------------
past_mid=0
mid=0
error=100
right_f=0
mid_f=0
left=0
right=0.11

right_f=f(right)

i=0;
while error>0.000000001:
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

print("Bisection Method: ",mid)


#-------------------------newton_raphson_method-----------------------------------------
past_mid=0.05
mid=0
error=100
left=0
right=0.11

i=0;
while error>0.0000000001:
    mid = past_mid - f(past_mid) / fprime(past_mid)

    error =( abs(mid - past_mid) / mid) * 100
    past_mid = mid
    i=i+1

print("Newton_Raphson Method: ",mid,'\n')