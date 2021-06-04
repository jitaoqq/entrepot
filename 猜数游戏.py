import random
num = random.randint(0,100)
cs = 0
ed = 2000
while True:
    cs = cs + 1
    ed = ed - 500
    a = input("请输入一个数:")
    a = int(a)
    if a > num:
        print("大了")
    elif ed < 500:
        print("您的余额不足请及时充值")
        break
    elif a < num:
        print("小了")
    elif ed < 500:
        print("您的余额不足请及时充值")
        break
    else:
        ed = ed + 200
        print("答对了，用了", cs, "次")
        break


