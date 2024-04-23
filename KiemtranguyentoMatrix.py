from math import *
def nt(n):
    if n<2:
        return False
    for i in range(2,int(sqrt(n)+1)):
        if n%i==0:
            return False
    return True


if __name__ == '__main__':
    n,m = map(int,input().split())
    a = list()
    for i in range(m):
        b = list(map(int,input().split()))
        a.append(b)
    for i in range(n):
        for j in range(m):
            if nt(a[i][j]):
                a[i][j] = 1
            else:
                a[i][j] = 0
    for i in range(n):
        for j in range(m):
            print(a[i][j],end=' ')
        print()