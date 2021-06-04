def a(b):
    nn = {}
    for i in b:
        k=0
        for j in b:
            if i==j:
                k=k+1
                nn[i] = k
    return nn

kljh=[1,2,3,5,6,2,1,3,4]
print(a(kljh))
