def main():
    t = int(input())
    for i in range(0, t):
        n, m, p = map(int, input().split())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        c = list(map(int, input().split()))
        x = 0
        y = 0
        z = 0
        res = list()
        while x < n and y < m and z < p:
            if a[x] == b[y] == c[z]:
                res.append(a[x])
                x += 1
                y += 1
                z += 1
            elif a[x] > b[y]:
                y += 1
            elif b[y] > c[z]:
                z += 1
            elif c[z] > a[x]:
                x += 1
        if len(res) != 0:
            for i in res:
                print(i, end = " ")
            print()
        else:
            print("NO")

main()