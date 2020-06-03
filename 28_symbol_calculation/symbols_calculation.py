#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 11:24:20 2020

@author: user
"""
from sympy import *
import numpy as np
# from numpy.linalg import inv

fx, fy, cx, cy, M, M_N, M_NT, B = symbols('fx, fy, cx, cy, M, M_N, M_NT, B')
# fy = symbols('fy')
# sympy 和 numpy 都可以建立带符号的矩阵，但是 numpy 无法对带符号的矩阵进行求逆运算
# sympy
M = Matrix([[fx, 0, cx], [0, fy, cy], [0, 0, 1]])
M_N = M**-1
M_NT = M_N.T
B = M_NT * M_N

# numpy
# M = np.mat([[fx, 0, cx], [0, fy, cy], [0, 0, 1]])
# k = np.mat([[1,0,0],[0,1,0],[0,0,1]])
# M_N = np.linalg.inv(k)

print('M = ')
print(M)
print('M_N = ')
print(M_N)
print('M_NT = ')
print(M_NT)
print('B = ')
print(B)