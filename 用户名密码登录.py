name = "admin"
password = "root"
a = 0

while True:
    c = input("请输入用户名:")
    b = input("密码:")
    a = a+1
    if a == 3:
        print("您的机会已用完")
        break
    elif c != name and b != password:
        print("用户名错误或密码错误")
    else:
        print("登录成功")
        break



