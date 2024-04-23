if __name__ == '__main__': # tính ans[0] xong suy ra còn lại
    n = int(input())
    a = list()
    ans = list()
    for _ in range(n):
            b = list(map(int,input().split()))
            a.append(b)
    if n==2:
        print("1 1")
    else:
        ans.append((a[0][1]+a[0][2]-a[1][2]) // 2)
        for i in range(1,n):
            ans.append(a[0][i]-ans[0])
        for ans1 in ans:
            print(ans1,end=' ')
    