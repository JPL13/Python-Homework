#%%
def f(x):
    return x**2-1

#%%
def df(x):
    return 2*x

#%%
def newton(f, df, xnod, e):
    delta=abs(f(xnod))
    while delta>e:
        xnod=xnod-float(f(xnod))/df(xnod)
        delta=abs(f(xnod))
    return xnod
    
#%%
print newton(f, df, 3, 0.0001)
print newton(f, df, -.5, 0.0001)

#%%
def g(x):
    import math
    return math.sin(x)
def dg(x):
    import math
    return math.cos(x)
print newton(g, dg, 2, .0001)

#%%
def h(x):
    import math
    return math.log(x)-1

def dh(x):
    return 1/x

print newton(h, dh, 1.5, .0001)

#%%
def solve(func, x0, e):
    delta=abs(func(x0)[0])
    while delta>e:
        x0=x0-float(func(x0)[0])/func(x0)[1]
        delta=abs(func(x0)[0])
    return x0
   
 #%%   
print solve(lambda x: [x**2-1, 2*x], 3, 0.0001)
