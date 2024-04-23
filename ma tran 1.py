n = int(input())
a = list()
for i in range(n):
    b = list(map(int,input().split()))
    a.append(b)
k = int(input())
sum_up , sum_down = 0,0
for i in range(n):
    for j in range(n):  
        if i+j<n-1:
            sum_up += a[i][j]
        elif i+j>n-1:
            sum_down += a[i][j]
ans = abs(sum_up-sum_down)
if ans <= k:
    print("YES")
    print(abs(ans))
else:
    print("NO")
    print(abs(ans))
    