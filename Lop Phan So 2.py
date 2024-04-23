from math import *

class Ps:
    def __init__(self,tu1,mau1,tu2,mau2):
        self.__tu1 = tu1
        self.mau1 = mau1
        self.tu2 = tu2
        self.mau2 = mau2
    def tu_moi(self):
        return self.tu1*self.mau2 + self.tu2*self.mau1
    def mau_moi(self):
        return self.mau1*self.mau2
    def ketqua(self):
        ucln = gcd(self.tu_moi(),self.mau_moi())
        tuso = self.tu_moi() // ucln 
        mauso = self.mau_moi() // ucln
        return f'{tuso}/{mauso}'

def nt(Ps):
    print(Ps._tu1)

if __name__ == '__main__':
    a,b,c,d = map(int,input().split())
    phanso = Ps(a,b,c,d)
    print(phanso.ketqua())
    nt(phanso)