if __name__ == '__main__':
    test = int(input())
    a = {}
    for _ in range(test):
        ma_mon = input()
        ten_mon = input()
        thi = input()
        a[ma_mon] = (ten_mon,thi)
    ans = list(a.items())
    ans.sort()
    for key,val in ans:
        print(key,end=' ')
        for res in val:
            print(res,end=' ')
        print()