if __name__ == '__main__':
    test = int(input())
    dp = {}
    for _ in range(test):
        s1 = input()
        for i in s1:
            if not i.isalpha():
                s1 = s1.replace(i,' ')
        s = s1.split()
        for res1 in s:
            res = res1.lower()
            if res in dp:
                dp[res]+=1
            else:
                dp[res] = 1
    a = list(dp.items())
    a.sort(key = lambda x: (-x[1],x[0]))
    for key,value in a:
        if not key.isalpha():
            continue
        else:
            print(key,value)