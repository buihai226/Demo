if __name__ == '__main__':
    ans = list()
    a = {} # lưu kết quả
    diemcc = {} # tính điểm chuyên cần
    n = int(input())
    vitri = {}
    dem = 1
    for _ in range(n):
        msv = input()
        name = input()
        malop = input()
        diemcc[msv] = 10
        tmp = (msv,name,malop)
        a[msv] = (name,malop)
        vitri[msv] = dem
        dem += 1
    for _ in range(n):
        res = input().split() # res[0] = msv
        res1 = res[1]
        for tmp in res1:
            if tmp == 'v':
                diemcc[res[0]] -= 2
            elif tmp == 'm':
                diemcc[res[0]] -= 1
            else:
                continue
        tmp = (res[0],a[res[0]],diemcc[res[0]],vitri[res[0]])
        ans.append(tmp)
    ans.sort(key = lambda x : x[3])
    for ans1,ans2,ans3,ans4 in ans:
        print(ans1,end=' ')
        for abc in ans2:
            print(abc,end=' ')
        if ans3 <= 0:
            print("0 KDDK")
        else:
            print(ans3)
        
    
        