from math import *

def nt(n1):
    if n1<2: return False
    for i in range(2,int(sqrt(n1)+1)):
        if n1%i==0:
            return False
    return True


if __name__ == '__main__':
    n,m = map(int,input().split())
    a = list()
    max_cnt = 0
    check = False
    for i in range(n):
        b = list(map(int,input().split()))
        for res in b:
            if nt(res) and max_cnt < res:
                check = True
                max_cnt = res
        a.append(b)
    if check == True: 
        print(max_cnt)
        for i in range(n):
            for j in range(m):
                if a[i][j] == max_cnt:
                    print("Vi tri [",i,'][',j,']',sep="")
    else:
        print('NOT FOUND')
    