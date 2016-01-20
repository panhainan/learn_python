# -*- coding: utf-8 -*-

def power(x,n=2):
    sum = 1
    while n>0:
        n = n-1
        sum *=x
    return sum

