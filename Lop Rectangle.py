class Rectangle:
    def __init__(self,cd,cr,clr):
        self.cd = cd
        self.cr = cr
        self.clr = clr
    def perimeter(self):
        return (self.cd+self.cr)*2
    def area(self):
        return self.cd * self.cr
    def color(self):
        ans = self.clr.title()
        return ans



arr = input().split()
if int(arr[0]) > 0 and int(arr[1]) > 0:
    r = Rectangle(int(arr[0]), int(arr[1]), arr[2])
    print("{} {} {}".format(r.perimeter(), r.area(), r.color()))
else:
    print("INVALID")