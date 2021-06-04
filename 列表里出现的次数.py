'''
a=[1,4,7,5,8,2,1,3,4,5,9,7,6,1,10]
b=len(a)
i=0
while i<b:
    j=0
    while j<b:
        if a[b-1]==a[j]:
            print(a[b-1],"出现",j+1,end="")
            j=j+1
    print()


    i=i+1
'''
import collections

a = [5,2,4,8,6,2,1,4,7,5,4,1,2,3,5,8,4,1,2]
b = collections.Counter(a)
for c in b:
    print(c,"出现",b[c],"次")