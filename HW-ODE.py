#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 17:02:34 2018

@author: AppleMoony
"""

import numpy as np

m = 1.0
g = 1.0
l = 1.0

p1 = m
p2 =g
p3 =l

c = p2/p3

def pend(y, t):
    y1, y2 = y
    dydt = [y2,  - c*np.sin(y1)]
    return dydt

# Intitial condition
y0 = [1.0, 0.0]
print(y0)

t = np.linspace(0, 10, 101)

from scipy.integrate import odeint
sol = odeint(pend, y0, t)

plt.plot(t, sol[:, 0], 'k',label='theta(t)')
plt.xlabel("t")
plt.ylabel("theta")
plt.show()