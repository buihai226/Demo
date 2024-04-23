from math import *

n=int(input())
a=[]
dem=0
for i in range (n):
    s=input()
    b=s.count("C")
    dem+=int((b*(b-1))/2)
    a.append(s)
for i in range (n):
    c=0
    for j in range (n):
        if (a[j][i]=="C"):
            c+=1
    dem+=int((c*(c-1))/2)   
print(dem)