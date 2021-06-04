语文 = ['小明','小张','小黄','小杨']
数学 = ['小黄','小李','小王','小杨','小周']
英语 = ['小杨','小张','小吴','小冯','小周']
li = 语文 + 数学 + 英语
ll=语文 + 英语
# 求选课学生总共有多少人
# 求只选了第一个学科的人的数量和对应的名字
# 求只选了一门学科的学生的数量和对应的名字
# 求只选了语文和英语的学生的数量和对应的名字

# num = 0
# peonum = []
# for i in 语文:
#         peonum.append(i)
#         num = num + 1
# for i in 数学:
#     if i not in peonum:
#         peonum.append(i)
#         num = num + 1
# for i in 英语:
#     if i not in peonum:
#         peonum.append(i)
#         num = num + 1
# print("选课的人数为：", num)


# i=0
# while i<len(语文):
#     print(语文[i],end="")
#     i=i+1
# else:
#     print(i)


# i = 0
# while i < len(li):
#     count = 0
#     # 排重
#     k = 0
#     flag = 0
#     while k < i:
#         if li[i] == li[k]:
#             flag = 1
#             break
#         k = k + 1
#     if flag == 1:
#         i = i + 1
#         continue # 终止后面的程序，直接进行下一轮
#     # 统计
#     j = i
#     while j < len(li):
#         if li[i] == li[j]:
#             count = count + 1
#         j = j + 1
#     if count==1:
#         print(li[i])
#     i = i + 1


i = 0
while i < len(ll):

    # 排重
    k = 0
    flag = 0
    while k < i:
        if ll[i] == ll[k]:
            flag = 1
            break
        k = k + 1
    if flag == 1:
        i = i + 1
        continue # 终止后面的程序，直接进行下一轮
    # 统计
    j = i
    count = 0
    while j < len(ll):
        if ll[i] == ll[j]:
            count = count + 1
        j = j + 1
    print(ll[i])

    i = i + 1
print(i)


