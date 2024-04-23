if __name__ == '__main__':
    n = int(input())
    a = list()
    for _ in range(n):
        b = list(map(int,input().split()))
        a.append(b)
    k = int(input())
    sum_up , sum_down = 0,0
    for i in range(n):
        for j in range(n):
            if i>j:
                sum_down += a[i][j]
            elif i<j:
                sum_up += a[i][j]
            else:
                continue
    ans = abs(sum_up-sum_down)
    if ans > k:
        print('YES',ans,end="\n")
    else:
        print("NO",ans,end="\n")