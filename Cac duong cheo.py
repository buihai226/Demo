if __name__ == '__main__':
    n = int(input())
    a = []  # list kết quả
    
    for i in range(n):
        row = [0] * n
        a.append(row)
    for i in range(n):
        a[i][i] = 0
    for i in range(1, n):
        for j in range(n-i):
            a[j][j+i] = i
            a[j+i][j] = i
    for row in a:
        print(*row)