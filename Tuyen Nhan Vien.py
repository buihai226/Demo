class Staff:
    def __init__(self,name,lt,th):
        self.name = name
        self.lt = lt
        self.th = th
    def grade(self):
        lt1 = float(self.lt)
        th1 = float(self.th)
        if lt1>10:
            lt1 /= 10
        if th1 > 10:
            th1 /= 10
        return (lt1+th1)/2
    def kq(self):
        res = self.grade()
        if res < 5:
            return "TRUOT"
        elif 5 <= res <8:
            return "CAN NHAC"
        elif 8<= res <= 9.5:
            return "DAT"    
        elif res > 9.5:
            return "XUAT SAC"



if __name__ == '__main__':
    a = list()
    test = int(input())
    vt = 1
    for _ in range(test):
        s = Staff(input(),float(input()),float(input()))
        id = "TS0"
        id += str(vt)
        vt += 1
        tmp = (id,s.name,s.grade(),s.kq())
        a.append(tmp)
    a.sort(key = lambda x : -x[2])
    for a1,a2,a3,a4 in a:
        print("{} {} {:.2f} {}".format(a1,a2,a3,a4))