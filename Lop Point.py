from math import *
from decimal import Decimal
class Point:
    def __init__(self,x,y): # hàm định nghĩa lớp Point có những gì
        self.x = x #public
        self.y = y
    def distance(self,other): # other là 1 Point khác
        ans = sqrt((self.x-other.x)**2 + (self.y-other.y)**2)
        return f'{ans:.4f}'
        
    
    
if __name__ == '__main__':
    t = int(input())
    while t > 0:
        arr = input().split()
        p1 = Point(Decimal(arr[0]), Decimal(arr[1]))
        p2 = Point(Decimal(arr[2]), Decimal(arr[3]))
        print(p1.distance(p2))
        t -= 1
        
    