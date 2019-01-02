#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 28 10:25:58 2018

@author: AppleMoony
"""

from  sympy  import  *

w, t, T, Ie, T0, P=symbols('w, t, T, Ie, T0, P')
e11=diff(w(t), t)-T/Ie
e12=T0*(1-(w(t)*T0/(4*P)))
e13=e11.subs(T, e12)
e14=dsolve(e13, w(t))

C1 = symbols('C1')

C1sub=solve(e14.rhs.subs(t, 0), C1)[0]

e14=e14.rhs.subs(C1, C1sub)

T=e12.subs(w(t), e14)

var("tf")

e15=simplify(integrate(T, (t, 0, tf ), conds='none'))

de15 = diff(e15,T0)

e18 = solve(de15,T0)

print simplify(e18[1])