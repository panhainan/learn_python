#-*-coding:utf-8-*-

from functools import reduce

def prod(L):
    def prodxy(x,y):
        return x*y
    return reduce(prodxy,L)
