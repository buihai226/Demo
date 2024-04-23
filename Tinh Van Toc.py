class Person:
    def __init__(self,name,home,time):
        self.name = name
        self.home = home
        self.time = [int(x) for x in time]
    def thoigian(self): # trả về số phút đi hết quãng đường
        gio = int(self.time[0])
        phut = int(self.time[1])
        ans1 = int(gio*60 + phut - 6*60)
        return ans1
    def speed(self):
        res = self.thoigian()
        sp = 120/res*60 # tốc độ cần tìm 
        return sp
    def id(self): # mã của người
        ans = ""
        for res in self.home:
            ans += res[0].upper
        for res in self.name:
            ans += res[0].upper()
        return ans
    
if __name__ == '__main__':
    test = int(input())
    a = list()
    for _ in range(test):
        s = Person(input().split(),input().split(),input().split(":"))
        b = (s.id()," ".join(s.name)," ".join(s.home),round(s.speed()))
        a.append(b)
    a.sort(key = lambda x : -x[3])
    for a1,a2,a3,a4 in a:
        print("{} {} {} {} Km/h".format(a1,a2,a3,a4))
        
    