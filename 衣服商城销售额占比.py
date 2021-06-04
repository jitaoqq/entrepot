id1 = 1
name1 = "羽绒服"
price1 = 253.6
num1 = 500
quan1 = 10


id2 = 2
name2 = "风衣"
price2 = 96.8
num2 = 335
quan2 = 43


id3 = 3
name3 = "皮草"
price3 = 135.9
num3 = 855
quan3 = 63


id4 = 4
name4 = "T血"
price4 = 65.8
num4 = 632
quan4 = 63


id5 = 5
name5 = "衬衫"
price5 = 49.3
num5 = 562
quan5 = 120


id6 = 6
name6 = "牛仔裤"
price6 = 86.3
num6 = 600
quan6 = 60

print("==========================衣服商城===================================================================")
print("----------------------------------------------------------------------------------------------------")
print("  日期          名称          单价          库存           日销售量  ")
print("  ",id1,"        ",name1,"       ",price1,"       ",num1,"        ",quan1,"          ")
print("  ",id2,"        ",name2,"       ",price2,"       ",num2,"        ",quan2,"          ")
print("  ",id3,"        ",name3,"       ",price3,"       ",num3,"        ",quan3,"          ")
print("  ",id4,"        ",name4,"       ",price4,"       ",num4,"        ",quan4,"          ")
print("  ",id5,"        ",name5,"       ",price5,"       ",num5,"        ",quan5,"          ")
print("  ",id6,"        ",name6,"       ",price6,"       ",num6,"        ",quan6,"          ")
print("-----------------------------------------------------------------------------------------------------")
print("羽绒服销售占比：",round(((quan1/(quan1+quan2+quan3+quan4+quan5+quan6))*100),1),"%")
print("风衣销售占比：",round(((quan2/(quan1+quan2+quan3+quan4+quan5+quan6))*100),1),"%")
print("皮草销售占比：",round(((quan3/(quan1+quan2+quan3+quan4+quan5+quan6))*100),1),"%")
print("T血销售占比：",round(((quan4/(quan1+quan2+quan3+quan4+quan5+quan6))*100),1),"%")
print("衬衫销售占比：",round(((quan5/(quan1+quan2+quan3+quan4+quan5+quan6))*100),1),"%")
print("牛仔裤销售占比：",round(((quan6/(quan1+quan2+quan3+quan4+quan5+quan6))*100),1),"%")
print("-------------------------------------------------------------------------------------")
print("羽绒服销售额占比：",round((((quan1*price1)/((quan1*price1)+(quan2*price2)+(quan3*price3)+(quan4*price4)+(quan5*price5)+(quan6*price6)))*100),1),"%")
print("风衣销售额占比：",round((((quan2*price2)/((quan1*price1)+(quan2*price2)+(quan3*price3)+(quan4*price4)+(quan5*price5)+(quan6*price6)))*100),1),"%")
print("皮草销售额占比：",round((((quan3*price3)/((quan1*price1)+(quan2*price2)+(quan3*price3)+(quan4*price4)+(quan5*price5)+(quan6*price6)))*100),1),"%")
print("T血销售额占比：",round((((quan4*price4)/((quan1*price1)+(quan2*price2)+(quan3*price3)+(quan4*price4)+(quan5*price5)+(quan6*price6)))*100),1),"%")
print("衬衫销售额占比：",round((((quan5*price5)/((quan1*price1)+(quan2*price2)+(quan3*price3)+(quan4*price4)+(quan5*price5)+(quan6*price6)))*100),1),"%")
print("牛仔裤销售额占比：",round((((quan6*price6)/((quan1*price1)+(quan2*price2)+(quan3*price3)+(quan4*price4)+(quan5*price5)+(quan6*price6)))*100),1),"%")


