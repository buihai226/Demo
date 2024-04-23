if __name__ == '__main__':
    n,m = map(int,input().split())
    a = list() # list ban đầu
    for i in range(n):
        b = list(map(int,input().split()))
        a.append(b)
    if n == m:
        for i in range(n):
            for j in range(m):
                print(a[i][j],end=' ')
            print()
    elif n>m:
        dem = n-m # số hàng thừa
        ans = list()
        t = 0 # hàng đang xét
        while dem>0:
            ans.append(t)
            dem -= 1
            t += 2
        res = list()
        for i in range(n):
            if i in ans:
                continue
            else:
                res.append(a[i])
        for i in range(m):
            for j in range(m):
                print(res[i][j],end=' ')
            print()
    elif m>n:
        dem = m-n # số cột thừa
        ans = list() # lưu hàng cần xóa
        t = 1
        while dem >0:
            ans.append(t)
            dem -= 1
            t +=2
        res = list()
        for i in range(n):
            res1 = list()
            for j in range(m):
                if j in ans:
                    continue
                else:
                    res1.append(a[i][j])
            res.append(res1)
        for i in range(n):
            for j in range(n):
                print(res[i][j],end=' ')
            print()
        