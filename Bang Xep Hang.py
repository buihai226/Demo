if __name__ == '__main__':
    test = int(input())
    dp = {}
    ans = list()
    for _ in range(test):
        s1 = input()
        s2 = list(map(int,input().split()))
        a = (str(s1),s2[0],s2[1])
        ans.append(a)
    ans.sort(key = lambda x : (-x[1],x[2],x[0]))
    for x,y,z in ans:
        print(x,y,z,sep=' ')