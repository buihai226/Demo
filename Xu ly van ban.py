if __name__ == '__main__':
    test = int(input())
    dp = {}
    abc = ()
    print(type(abc))
    for _ in test:
        s1 = input().split().title()
        s2 = map(int,input().split())
        dp[s1] = (s2[0],s2[1])