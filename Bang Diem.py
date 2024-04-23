class Student:
    def __init__(self,ten,diem):
        self.ten = ten
        self.diem = diem
    def diem_tb(self):
        res = 0
        res += float(self.diem[0])*2
        res += float(self.diem[1])*2
        for i in range(2,len(self.diem)):
            res += float(self.diem[i])
        dapan = round(res/10/1.2,1)
        return dapan
    def get_ten(self):
        return self.ten
    def ketqua(self):
        ans = float(self.diem_tb())
        if ans >= 9:
            return 'XUAT SAC'
        elif 8<=ans<=8.9:
            return 'GIOI'
        elif 7<=ans<=7.9:
            return 'KHA'
        elif 5<=ans<=6.9:
            return "TB"
        elif ans<5:
            return "YEU"
    
    
    
if __name__ == '__main__':
    test = int(input())
    id = 1
    ans = list()
    for _ in range(test):
        m = input()
        n = input().split()
        s = Student(m,n)
        t = (id,s.get_ten(),s.diem_tb(),s.ketqua())
        ans.append(t)
        id+=1
    ans.sort(key = lambda x:(-x[2],x[0]))
    for a1,a2,a3,a4 in ans:
        if int(a1) < 10:
            print('HS0{} {} {:.1f} {}'.format(a1,a2,a3,a4))
        else:
            print('HS{} {} {:.1f} {}'.format(a1,a2,a3,a4))
    
    
        