#-*-coding:utf-8-*-
def calc(*numbers):
    sum=0
    for n in numbers:
        sum = sum + n*n
    print("计算平方和")
    return sum
    
