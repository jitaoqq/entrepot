z=input("输入一个数：")
z=int(z)
o=1
while o<=z:
    k=1
    j=z
    while j >= o:
        print(" ", end="")
        j=j-1
    while k<=o:
        print("* ",end="")
        k=k+1
    print()
    o=o+1



