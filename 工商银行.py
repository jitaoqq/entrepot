import random
# 银行的库
names = {}
'''
{
    "张三":{address:"沙河北大桥桥底下",money:546,account:1a5sdf1af},
    "张三":{address:"沙河北大桥桥底下",money:546}
}
'''

# 开户行名称
bank_name = "中国工商银行昌平支行"
# 欢迎页面的模板
welcome = '''
    -----------------------------------------
    -     欢迎来到中国工商银行账户管理系统     -
    -----------------------------------------
    -   1.开户                               -
    -   2.存钱                               -
    -   3.取钱                               -
    -   4.转账                               -
    -   5.查询                               -
    -   6.Bye!                               -
    ------------------------------------------
'''

# 创建随机账户
def getRandom():
    li = ["1","2","3","4","5","6","7","8","9","0","a","b","c","d","e","f"]
    string = ""
    for i in range(8):
        ch = li[random.randint(0,len(li) - 1)]
        string = string +  ch
    return string

# 银行的开户逻辑
def bank_addUser(account,username,password,money,country,province,street,door):
    # 1.判断是否已满
    if len(names)  >= 100:
        return 3
    # 2.判断是否存在:依据是用户名
    if username in names:
        return 2
    # 3.开户
    names[username] = {
        "account":account,
        "username":username,
        "password":password,
        "money":money,
        "country":country,
        "province":province,
        "street":street,
        "door":door,
        "bank_name":bank_name
    }
    return 1


# 开户操作
def addUser():
    username = input("请输入您的姓名：")
    password = input("请输入你的密码：")
    money = int(input("请输入您的账户余额：")) # "123"  123
    print("下面请输入您的个人地址信息：")
    country = input("请输入您的国籍：")
    province =  input("请输入您的省份：")
    street = input("请输入您的居住街道：")
    door = input("请输入您的门牌号：")
    account = getRandom()
    status = bank_addUser(account,username,password,money,country,province,street,door)
    if status == 1:
        print("恭喜开户成功！以下是您的个人信息：")
        info = '''
            ----------个人信息 【工商银行】--------
            用户名：%s,
            密码：%s,
            账号：%s,
            余额：%s,
            国家：%s,
            省份：%s,
            街道:%s,
            门牌号：%s
            开户行名称：%s
            ------------------------------------
        '''
        print(info % (username,password,account,money,country,province,street,door,bank_name))

    elif status == 2:
        print("对不起，您的账户已存在！请勿重复开户！")
    elif status == 3:
        print("对不起，用户库已满，请携带证件到其他银行办理！")
#========================================================================================================

# 存钱逻辑判断
def cqlj(password,money,username,account):
    if account not in names[username]['account']:
        return 2
    if password not in names[username]['password']:
        return 3
    if account in names[username]['account'] and password in names[username]['password']:
        return 1


# 存钱操作方法
def cunqian():
    username = input("请输入您的姓名：")
    account = input("请输入您的账户：")
    password = input("请输入你的密码：")
    money = int(input("请输入您的存款额："))
    status = cqlj(password,money,username,account)
    if status == 1:
        money = money + names[username]['money']
        print("恭喜存钱成功！",money)
    elif status == 2:
        print("对不起，您的账户不存在！")
    elif status == 3:
        print("对不起，您的密码不正确！")

#取钱逻辑
def qqlj(password,money,username,account):
    if money <= names[username]['money']:
                return 1
    if account not in names[username]['account']:
        return 2
    if password not in names[username]['password']:
        return 3
    if money > names[username]['money']:
        return 4
#取钱方法
def quqian():
    username = input("请输入您的姓名：")
    account = input("请输入您的账户：")
    password = input("请输入你的密码：")
    money=int(input("请输入您要取的金额："))
    status=qqlj(password,money,username,account)
    if status==1:
        money = names[username]['money'] - money
        print("取钱成功！您的余额为：",money)
    if status==2:
        print("账户错误")
    if status==3:
        print("密码错误")
    if status==4:
        print("余额不足")
#转账逻辑
def zzlh(password,money,username,account,account1,username1):
    if money <= names[username]['money']:
        return 1
    if account not in names[username]['account']:
        return 2
    if password not in names[username]['password']:
        return 3
    if money > names[username]['money']:
        return 4
    if account1 not in names[username]['account']:
        return 5
    if username not in names:
        return 6
    if username1 not in names:
        return 7



#转账方法
def zhuanz():
    username = input("请输入您的姓名：")
    account = input("请输入您的账户：")
    password = input("请输入你的密码：")
    username1=input("请输入对方的姓名：")
    account1 = input("请输入对方的账户：")
    money = int(input("请输入您要转的金额："))
    status=zzlh(password,money,username,account,account1,username1)
    if status==1:
        names[username1]['money'] = names[username1]['money'] + money
        money = names[username]['money'] - money

        print("转账成功！您的余额为：",money)
    if status==2:
        print("账户错误")
    if status==3:
        print("密码错误")
    if status==4:
        print("余额不足")
    if status==5:
        print("对方账户不正确")
    if status==6:
        print("您的姓名不存在")
    if status==7:
        print("对方姓名不正确")
#查询逻辑
def cxlj(username,account,password):
    if account not in names[username]['account']:
        return 2
    if password not in names[username]['password']:
        return 3
    if account in names[username]['account'] and password in names[username]['password']:
        return 1

#查询方法
def chax():
    username = input("请输入您的姓名：")
    account = input("请输入您的账户：")
    password = input("请输入你的密码：")
    status=cxlj(username,account,password)
    money=names[username]['money']
    country=names[username]['country']
    province=names[username]['province']
    street=names[username]['street']
    door=names[username]['door']
    if status==1:
        print("恭喜开户成功！以下是您的个人信息：")
        info = '''
                    ----------个人信息 【工商银行】--------
                    用户名：%s,
                    密码：%s,
                    账号：%s,
                    余额：%s,
                    国家：%s,
                    省份：%s,
                    街道:%s,
                    门牌号：%s
                    开户行名称：%s
                    ------------------------------------
                '''
        print(info % (username, password, account, money, country, province, street, door, bank_name))
    if status == 2:
        print("账户错误")
    if status == 3:
        print("密码错误")


# 入口程序
while True:
    print(welcome)
    chose = input("请输入您的业务编号：")
    if chose == '1':
        addUser()
    elif chose == '2':
        cunqian()
    elif chose == '3':
        quqian()
    elif chose == '4':
        zhuanz()
    elif chose == '5':
        chax()
    elif chose == '6':
        break
    else:
        print("输入非法！别瞎弄！")