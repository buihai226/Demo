s1= input().split()
h,m,s=int(s1[0]),int(s1[1]),int(s1[2])

do=(h%12)*30+m*0.5+s*0.5/60
print("Angle: ",do)