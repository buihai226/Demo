class Person:
    def __init__(self,id,name,start,end):
        self.id = id
        self.name = name
        self.start = start
        self.end = end
    def time(self):# trả về số giây sử dụng
        st1 = int(self.start[:2])# giờ bắt đầu
        st2 = int(self.start[3:])
        en1 = int(self.end[:2])#  giờ kết thúc
        en2 = int(self.end[3:])
        tmp = en1*3600+en2*60-st1*3600-st2*60
        return tmp
    def thoigian(self):
        res = self.time()
        gio = res // 3600
        phut = int((res - gio*3600)/60)
        return "{} gio {} phut".format(gio,phut)
        
if __name__ == '__main__':
    test = int(input())
    a = list()
    for _ in range(test):
        s = Person(input(),input(),input(),input())
        cnt = (s.id,s.name,s.time(),s.thoigian())
        a.append(cnt)
    a.sort(key = lambda x : -x[2])
    for res in a:
        print("{} {} {}".format(res[0],res[1],res[3]))