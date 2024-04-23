if __name__ == '__main__':
    test = int(input())
    for _ in range(test):
        n,m,k = map(int,input().split())
        a = list(map(int,input().split())) #n
        b = list(map(int,input().split())) #m
        c = list(map(int,input().split())) #k
        ans1 = list()
        for i in a:
            if i in b:
                ans1.append(i)
        ans2 = list()
        for i in ans1:
            if i in c:
                ans2.append(i)
        if len(ans2) > 0:
            for i in ans2:
                print(i,end=' ')
            print()
        else:
            print('NO')
            print()
        