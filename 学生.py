students = [
    {'name':'张三','age':23,'score':88,'tel':'23423532','gender':'男'},
    {'name':'李四','age':26,'score':80,'tel':'12533453','gender':'女'},
    {'name':'王五','age':15,'score':58,'tel':'56453453','gender':'男'},
    {'name':'赵六','age':16,'score':57,'tel':'86786785','gender':'保密'},
    {'name':'小明','age':18,'score':98,'tel':'23434656','gender':'女'},
    {'name':'小红','age':23,'score':72,'tel':'67867868','gender':'女'},
]
# c = 0
# gs=0
# a = students[c].get("score")
# b = students[c].get("age")
# wh= students[c].get("tel")
# d = 0
# o = 0
# while d < len(students):
#     a = students[c].get("score")
#     b = students[c].get("age")
#     wh= students[c].get("tel")
#     a = int(a)
#     b = int(b)
#     wh=int(wh)
#     if a < 60 :
#         print(students[c].get("name"),"分数为：",students[c].get("score"))
#         o = o + 1
#         c = c + 1
#         d = d+1
#     if b < 18:
#         gs = gs + 1
#     if a>=60:
#         c = c+ 1
#         d = d +1
#     if wh%10==8:
#         print("尾号为八的学生是：",students[c-1].get("name"))
# print("不及格的学生有：",o,"个。未成年有",gs,"个")
#====================================================================
# 统计最高分
# c=0
# d=0
# zgf=0
# a=students[c].get("score")
# while c<len(students):
#     a=students[c].get("score")
#     a=int(a)
#     if a>zgf:
#         zgf=a
#         k=students[c].get("name")
#         c=c+1
#         d=d+1
#
#     else :
#         c=c+1
#         d=d+1
#         continue
# print("最高分为：",k, zgf)
#===========================================================
#列表大小排序
# a=[]
# for i in range(len(students)):
#     for j in range(i,len(students)):
#         if students[i]["score"] < students[j]["score"]:
#
#             students[j],students[i] = students[i],students[j]
#             a=students
# print(a)
#----------------------------------------------------------------
#删除性别保密的学生
for i in students:
    if i['gender']=='保密':
        students.remove(i)
print(students)



# 1) 统计不及格学生的个数
# 2) b.打印不及格学生的名字和对应的成绩
# 3) 统计未成年学生的个数
# 4) 打印手机尾号是8的学生的名字
# 5) 打印最高分和对应的学生的名字
# 6) 将列表按学生成绩从大到小排序
# 7) 删除性别保密的所有学生
# a = len(students)
