#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 25 10:17:49 2018

@author: user
"""

from sympy import symbols
import sympy as sp
import numpy as np

# a = lastOsmX, b = lastOsmY, c = nextOsmX, d = nextOsmY 
a,b,c,d = symbols('a,b,c,d')
# e = lastOptX, f = lastOptY, g = nextOptX, h = nextOptY 
e,f,g,h = symbols('e,f,g,h')
# i = VOsm, j = VOpt, k = dotResult, l = disOpt, m = disOsm, n = cos
i,j,k,l,m,n = symbols('i,j,k,l,m,n')
i = [a-c,b-d]
j = [e-g,f-h]
k = (a-c)*(e-g)+(b-d)*(f-h)
# o=dcos/dlastOptX,p=dcos/dlastOptY,q=dcos/dnextOptX,r=dcos/dnextOptY
o,p,q,r = symbols('o,p,q,r')
# s=lastOsmX-nextOsmY=a-c, t=lastOsmY-nextOsmY=b-d, u=disOsm,v,w,x,y,z
s,t,u,v,w,x,y,z = symbols('s,t,u,v,w,x,y,z')
#s=a-c
#t=b-d
#u=sp.sqrt((a-c)**2+(b-d)**2)

# residual of angle
n = sp.acos((s*(e-g)+t*(f-h))/(u*sp.sqrt((e-g)**2+(f-h)**2)))

#print(n)

o = sp.diff(n,e)
p = sp.diff(n,f)
q = sp.diff(n,g)
r = sp.diff(n,h)
print(sp.sympify(o))
print(p)
print(q)
print(r)
