from scipy.integrate import trapz
from scipy.optimize import minimize, root, curve_fit
import numpy as np
import matplotlib.pyplot as plt

from scipy.linalg import norm
from scipy.spatial.distance import cdist
import scipy

N = 50
P= np.pi/2

#a. Generate arrays x ordered like [x1, x2, ..., xN-1, xN] and y ordered like [y1, y2, ..., yN-1, yN] to represent the unit quarter-circle with N points. 
x = np.zeros(N)

x = np.linspace(0, 1, N)
y=np.sqrt(1-x**2)
#print x
#print y

plt.axis('equal')
plt.plot(x, y, '-o')
#b. From these, generate an array z0, ordered like [xN, y1, y2, ..., yN-2, yN-1], that will be your (perfect) guess of the N decision variables.
z0 = np.zeros(N)
z0[0]=x[-1]
z0[1:]=y[:-1]# perfect guess
#print z0

#4. Write a function z2xy that calculates and returns the array of all the xs, [x1, x2, ..., xN-1, xN], 
#and all the ys ,[y1, y2, ..., yN-1, yN], given (as a parameter) an array z of decision variable values, 
#assuming they are ordered like [xN, y1, y2, ..., yN-2, yN-1].
def z2xy(z):
    x = np.zeros(N)
    y = np.zeros(N)
    x[-1]=z[0]
    x = np.linspace(0,x[-1],len(z))

#append yN to the list of ys from z
    
    y[:-1]=z[1:]
    y[-1]=0
    return x, y

x1, y1=z2xy(z0)

def obj(z):
    x1, y1=z2xy(z0)
    return -trapz(y1, x1)

obj(z0)

def con(z):
    x1, y1=z2xy(z0)
    dx=x[-1]/float((len(x1)-1))
    dy=np.diff(y1)
    dist = np.sum(np.sqrt(dx**2+dy**2))
    #print dist
    return round(dist-P)

con(z0)

bounds = [(0, P) for i in np.arange(N)]
print bounds

c1 = ({'type':'ineq', 'fun':con})
method = "slsqp"

sol = minimize(obj, z0, bounds = bounds, constraints = c1)
print sol

z0 = np.random.uniform(low=0., high=P, size=(50,))
z0[0]=P
print z0

sol = minimize(obj, z0, bounds = bounds, constraints = [c1], method=method)
#sol
x1, y1=z2xy(z0)
X=sol.x.sort()
ydata=np.sqrt(1-sol.x**2)

plt.axis('equal')
plt.plot(x1, y1, sol.x, ydata) 


    