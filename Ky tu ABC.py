def Try(n,s,a,b,c): # n là độ dài đang xét, s là xâu đang xét , a,b,c là số lượng A,B,C
    if len(s) == n and a>0 and a<=b and b<=c:
        print(s)
    if len(s) <n:
        Try(n,s+'A',a+1,b,c)
        Try(n,s+'B',a,b+1,c)
        Try(n,s+'C',a,b,c+1)
    
    
if __name__ == '__main__':
    n = int(input())
    for i in range(3,n+1):
        Try(i,'',0,0,0)