from math import *

def nt(n): # tính số lượng ước bằng tích (số mũ +1)
    res = 1
    for i in range(2,isqrt(n)+1):
        cnt = 0
        while n%i==0:
            cnt += 1
            n //= i
        if cnt != 0:
            res *= (cnt+1)
    if n != 1:
        res *= 2
    return res

if __name__ == '__main__':
    n1 = int(input())
    ans = 0
    for i in range(n1):
        if nt(i) == 9:
            ans +=1 
    print(ans)