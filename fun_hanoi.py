#-*-coding:utf-8-*-
def hanoi(n,a="A",b="B",c="C"):
    if n==1:
        print(a," --> ",c)
    else:
        hanoi(n-1,a,c,b)#将前n-1个盘子从x移动到y上
        hanoi(1,a,b,c)#将最底下的最后一个盘子从x移动到z上
        hanoi(n-1,b,a,c)#将y上的n-1个盘子移动到z上
    
    
