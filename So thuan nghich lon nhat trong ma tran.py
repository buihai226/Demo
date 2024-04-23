from math import *
def tn(n1):
    t = 0
    ans = n1
    while n1>0:
        t = t*10 + n1%10
        n1 //= 10
    if t == ans:
        return True
    else:
        return False 


if __name__ == '__main__':
    n,m = map(int,input().split())
    a = list()
    max_cnt = -1
    check = False
    for i in range(n):
        b = list(map(int,input().split()))
        for res in b:
            if tn(res) and max_cnt < res:
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
    