city = {
    "北京":{
        "昌平":{
            "天通苑":{"海底捞":[

                ['大锅',8],
                ['小锅',6]
                ],
                    "呷哺呷哺":{
                        '大份':80,
                        '小份':50
                   }
            },
            "龙泽":{"永辉超市":{
                '辣条':3,
                '干脆面':2
            },

                  "永旺超市":{
                      '白酒':45,
                      '红酒':20

                  }
            }
        },
        "海淀":{
            "公主坟":{"军事博物馆",

                   "中华世纪园"},
            "科普场馆":{"中国科技馆",

                    "北京天文馆"},
            "高校":{"北京大学",

                  "清华大学"}
        },
        "朝阳":{
            "龙城":{"鸟化石国家地质公园",

                  "朝阳南北塔"},
            "双塔":{"朝阳凌河公园",

                  "朝阳凤凰山"}
        }
    },
    "上海":{


    }
}
k=0
m=0
def qq(ss):
    for i in ss:
        print(i)
qq(city)
salary = input("请输入您的薪资：")
salary = int(salary)
a=input("请输入您去的地方:")
while True:
    if a in city:
        qq(city[a])
        a1=input("请输入在去的地方：")
        if a1 in city[a]:
            qq(city[a][a1])
            a2=input("请输入您还要去的地方：")

            if a2 in city[a][a1]:
                qq(city[a][a1][a2])
                a3=input("请选择购买的东西：")
                if a3 in city[a][a1][a2]:
                    mycart = []
                    while True:
                        for index, value in enumerate(city[a][a1][a2][a3]):
                            print(index, "", value)
                        num = input("请输入您要的商品编号：")
                        if num.isdigit():
                            num = int(num)
                            if num > len(city[a][a1][a2][a3]):
                                print("对不起，您要的商品不存在！请选择其他商品！")
                            else:
                                if salary < city[a][a1][a2][a3][num][1]:
                                    print("对不起，您的余额不足，穷鬼！")

                                elif city[a][a1][a2][a3][0] == city[a][a1][a2][a3][num][0] and k == 0:
                                    mycart.append(city[a][a1][a2][a3][num])
                                    salary = salary - (city[a][a1][a2][a3][num][1] / 2)
                                    m = m + (city[a][a1][a2][a3][num][1] / 2)
                                    print("恭喜您！添加成功！您的余额为：￥", salary)
                                    k = k + 1
                                else:
                                    mycart.append(city[a][a1][a2][a3][num])
                                    salary = salary - city[a][a1][a2][a3][num][1]
                                    m = m + city[a][a1][a2][a3][num][1]
                                    print("恭喜您！添加成功！您的余额为：￥", salary)
                        elif num == 'q' or num == 'Q':
                            print("欢迎下次光临!")
                            break
                        else:
                            print("输入非法，别瞎弄！请重新输入！")
                    print("您本次的购物情况如下：")
                    for index, value in enumerate(mycart):
                        print(index, "", value)
                    print("您的余额为：￥", salary, "您本次获得：", m, "积分")
                    break









