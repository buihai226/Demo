if __name__ == '__main__':
    n,m = map(int,input().split())
    a = list()
    min1,max1 = 10001,0
    for i in range(n):
        b = list(map(int,input().split()))
        max1 = max(max1,max(b))
        min1 = min(min1,min(b))
        a.append(b)
    res = max1-min1 #biến kết quả
    check = False #biến check
    for i in range(n):
        for j in range(m):
            if a[i][j] == res:
                check = True
                break
    if check == True:
        print(res)
        for i in range(n):
            for j in range(m):
                if a[i][j] == res:
                    print("Vi tri [{}][{}]".format(i,j))
    else:
        print('NOT FOUND') 