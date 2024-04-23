n = int(input())
res = ''
for i in range(0, n):
    s = input()
    res += s
ans = ''
for i in res:
    if i.isalpha():
        ans += ' '
    else:
        ans += i
a = list()
for i in ans.split():
    a.append(int(i))
a.sort()
for i in a:
    print(i)