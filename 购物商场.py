import random
n=random.randint(0,5)
a=[
    ["Iphone 12 pro",5],
    ["HUAWEI watch",5],
    ["lenovo pc",5],
    ["Mac pc",5],
    ["卫龙辣条",5],
    ["老干妈",5]
]
b=input("本店有免费的优惠券，每人限一张，要来一张吗！1 要 2 不要:")
b=int(b)
while b==1:
    print("恭喜你获得一张：",a[n][0],a[n][1],"折券")
    break
    if b==2:
        break
    else:
        break

m=0
k=0
shop = [
    ["Iphone 12 pro",12000],
    ["HUAWEI watch",2000],
    ["lenovo PC",5000],
    ["Mac pc",13000],
    ["卫龙辣条",5],
    ["老干妈",7.5]
]
for index,value in enumerate(shop):
    print(index,value)
salary = input("请输入您的薪资：")
salary = int(salary)
mycart = []
while True:
    for index,value in enumerate(shop):
        print(index,"",value)
    num = input("请输入您要的商品编号：")
    if num.isdigit():
        num = int(num)
        if num > len(shop):
            print("对不起，您要的商品不存在！请选择其他商品！")
        else:
            if salary < shop[num][1]:
                print("对不起，您的余额不足，穷鬼！")

            elif a[n][0] == shop[num][0] and k==0:
                mycart.append(shop[num])
                salary = salary - (shop[num][1]/2)
                m=m+(shoop[num][1]/2)
                print("恭喜您！添加成功！您的余额为：￥", salary)
                k=k+1
            else:
                mycart.append(shop[num])
                salary = salary - shop[num][1]
                m=m+shop[num][1]
                print("恭喜您！添加成功！您的余额为：￥", salary)
    elif num == 'q' or num == 'Q':
        print("欢迎下次光临!")
        break
    else:
        print("输入非法，别瞎弄！请重新输入！")
print("您本次的购物情况如下：")
for index,value in enumerate(mycart):
    print(index,"",value)
print("您的余额为：￥",salary,"您本次获得：",m,"积分")

