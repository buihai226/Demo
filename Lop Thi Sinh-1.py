class Sinhvien:
    def __init__(self,ten,ngaysinh,diem1,diem2,diem3):
        self.name = ten
        self.date = ngaysinh
        self.d1 = diem1
        self.d2 = diem2
        self.d3 = diem3
    def tong_diem(self):
        ans = float(self.d1)+float(self.d2)+float(self.d3)
        return ans
    def des(self):
        return f"{self.name} {self.date} {self.tong_diem():.1f}"
    
if __name__ == '__main__':
    s = Sinhvien(input(),input(),float(input()),float(input()),float(input()))
    print(s.des())
        