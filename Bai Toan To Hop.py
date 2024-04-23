def Try(index):
    if len(ans) == k:
        for ans1 in ans:
            print(ans1,end=' ')
        print()
    else:
        for i in range(index,len(a)):
            ans.append(a[i])
            Try(i+1)
            ans.pop()
         

if __name__ == '__main__':
    n,k=map(int,input().split())
    se = set(map(int,input().split()))
    a = list(se)
    a.sort()
    ans = []
    Try(0)