if __name__ == '__main__':
    n = int(input())
    a= list()
    while n>0:
        b = list(map(int,input().split()))
        x = len(b)
        for _ in b:
            a.append(_)
        n -= x
    check = False
    for i in range(1,max(a)+1):
        if not i in a:
            check = True
            print(i)
    if check == False:
        print('Excellent!')