# info = {
#     "苹果":32.8,
#     "香蕉":22,
#     "葡萄":15.5
# }
#
# value = info.values()
# key = info.keys()
# for ke in key:
#     ke = input("请输入您想购买的水果：")
#     print(info[ke])
Friuts = {
        "苹果":12.3,  # 水果和单价
        "草莓":4.5,
        "香蕉":6.3,
        "葡萄":5.8,
        "橘子":6.4,
        "樱桃":15.8
}
info = {
    '小明': {
        'fruits': {'苹果':4, '草莓':13, '香蕉':10},
        'money':0
    },
    '小刚': {
        'fruits': {'葡萄':19, '橘子':12, '樱桃':30},
        'money':23
    }
}

key=Friuts.keys()
value=Friuts.values()
ity = info['小明']['fruits'].keys()
imo = info['小明']['fruits'].values()
s=0
for i in ity:

    for ke in key:
        h=0
        if i==ke:
            h=h+(info['小明']['fruits'][i])*(Friuts[ke])
            s=s+h
info['小明']['money']=s
print(info)