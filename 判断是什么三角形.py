a = int(input("请输入一个数"))
b = int(input("请输入一个数"))
c = int(input("请输入一个数"))
if a+b>c and a+c>b and b+c>a:
    if c>b and c>a:
        if (a*a)+(b*b)==(c*c):
            print("是直角三角形")
    if b>a and b>c:
        if (a*a)+(c*c)==(b*b):
            print("是直角三角形")
    if a>b and a>c:
        if (b*b)+(c*c)==(a*a):
            print("是直角三角形")
    if a == b and b!=c:
            print("是等腰三角形")
    if b == c and c!=a:
            print("是等腰三角形")
    if a == c and c!=b:
            print("是等腰三角形")
    if a==b and b==c:
            print("是等边三角形")
    if a!=b and a!=c:
        print("普通三角形")
else:
    print("不构成三角形")

