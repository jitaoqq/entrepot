a=["张三","李四","王五","李六","亲叭"]
c=["撑死","饿死"]
import random
print("========================","斩首示众系统","============================")
while True:
    print("你怕了吗")
    i=input("输入1或2我将随机处死一个人或放一个人：")
    i=int(i)
    if i==1:
        d=random.randint(0,4)
        q=random.randint(0,1)
        print(a[d],"午时将开始实施",c[q],"刑法！！！")
        break
    elif i==2:
        d = random.randint(0, 4)
        q = random.randint(0, 1)
        print("恭喜你",a[d],"你将重获自由")
        break
    else:
        print("重新输入")
