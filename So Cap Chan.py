if __name__ == '__main__':
    n = int(input())
    a = list(map(int,input().split()))
    le,chan = 0,0
    for i in range(n):
        if a[i]%2==0:
            chan += 1
        else:
            le += 1
    ans = le*(le-1)/2 + chan*(chan-1)/2
    print(int(ans))