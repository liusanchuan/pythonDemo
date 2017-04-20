__author__ = 'Administrator'
import math

def pow23(x,m):
    s=1
    while m>0:
        m=m-1
        s=s*x
    return s
a=pow23(12,3)
print(a)

