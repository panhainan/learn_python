# -*- coding: utf-8 -*-

from functools import reduce
import math

def str2float(s):
    def int2float(x,y):
        return x+y/math.pow(10,len(str(y)))
    def str2int(s):
        def fn(x, y):
                return x * 10 + y
        def char2num(s):
            return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
        return reduce(fn,map(char2num,s))
    return reduce(int2float,map(str2int,s.split('.')))
