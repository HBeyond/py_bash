#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  1 11:16:45 2019

@author: user
"""
from sympy import symbols
import sympy as sp

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
n = sp.asin(sp.sqrt((s*(f-h)-(e-g)*t)**2)/(u*(sp.sqrt((e-g)**2+(f-h)**2))))

print(sp.diff(n,e)) # dr/dx1
print(sp.diff(n,f)) # dr/dy1  
print(sp.diff(n,g)) # dr/dx2
print(sp.diff(n,h)) # dr/dy2

