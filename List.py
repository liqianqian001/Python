# namelist = []   # 定义一个空列表
# namelist = ["小张", "小王", "小李" ]
'''
print(namelist[0])
print(namelist[1])
print(namelist[2])
testlist = [1, "测试"]    # 列表中可以存储混合类型
print(type(testlist[0]))
print(type(testlist[1]))
'''
# 用for和while遍历列表
'''
for name in namelist:
    print(name)
'''
'''
lenth = (len(namelist))    # len()可以得到列表的长度
i = 0
while i < lenth:
    print(namelist[i])
    i += 1
'''
# 增：    【append】
'''
print("----增加前.名单列表的数据----")
for name in namelist:
    print(name)
nametemp = input("请输入添加学生的姓名：")
namelist.append(nametemp)   # 在末尾增加一个元素
print("----增加后.名单列表的数据----")
for name in namelist:
    print(name)
'''

# 增：    【extend】
'''
a = [1, 2]
b = [3, 4]
a.append(b)     # 将b列表当作一个元素，加入到a列表中
print(a)
a.extend(b)     # 将b列表中的每个元素逐一追加到a列表中
print(a)
'''
# 增：    【insert】
'''
a = [0, 1, 2]
a.insert(1, 3)      # 第一个变量表示下标，第二个表示元素（对象）
print(a)        # 指定下标位置插入元素
'''


# 删     【del】【pop】
'''
movieName = ["加勒比海盗", "黑客帝国", "第一滴血", "指环王", "速度与激情", "指环王"]
print("----删除前.电影列表的数据----")
for name in movieName:
    print(name)

# del movieName[2]   # 在指定位置删除一个元素
# movieName.pop()     # 弹出（删除）末尾最后一个元素
movieName.remove("指环王")     # 直接删除指定内容的元素

print("----删除后.电影列表的数据----")
for name in movieName:
    print(name)
'''

# 改
'''
print("----修改前.名单列表的数据----")
for name in namelist:
    print(name)
    
namelist[1] = "小红"      # 修改指定下标的元素内容

print("----修改后.名单列表的数据----")
for name in namelist:
    print(name)
'''

'''
# 查     【in ， not in】
findName = input("请输入要查找的学生姓名：")

if findName in namelist:
    print("在学员名单中找到了相同的名字")
else:
    print("没有找到")
'''

'''
myList = ["a", "b", "c", "a", "b"]


print(myList.index("a", 1, 4))       # 可以查找指定下标范围的元素，并返回找对对应数据的下标

print(myList.index("a", 1, 3))      # 范围区间，左闭又开 【1，3）
                                    # 找不到会报错
                                    
print(myList.count("c"))        # 统计某个元素出现几次
'''

# 排序和反转
'''
a = [1, 4, 2, 3]
print(a)

a.reverse()     # 将列表所有元素反转
print(a)

a.sort()        # 升序
print(a)

a.sort(reverse=True)        # 降序
print(a)
'''

'''
# schoolName = [[], [], []]        # 有3个元素的空列表，每个元素是一个空列表
schoolName = [["北京大学", "清华大学"], ["南开大学", "天津大学", "天津师范大学"], ["山东大学", "中国海洋大学"]]

print(schoolName[0][0])
'''

# 课堂练习：将7个老师a～g，随机分配给3个办公室
'''
import random

teacher = ["a", "b", "c", "d", "e", "f", "g"]
offices = [[], [], []]

for teacherName in teacher:         # 遍历7个老师
    index = random.randint(0, 2)        # 取0到2的随机值作为办公室下标
    offices[index].append(teacherName)      # 将遍历到的老师按照随机的下标追加到对应办公室
print(offices)

i = 1
for office in offices:      # 遍历每个办公室
    print("办公室%d的人数为：%d"%(i, len(office)))      # len得到列表长度，并打印
    i += 1
    for name in office:         # 遍历办公室的老师
        print("%s"%name, end="\t")      # 打印每个老师的名字
    print("\n")
    print("-"*20)
'''


# 作业：
# 现有商品列表如下：
# 1.products = [["iphone", 6888], ["MacPro", 14800], ["小米6", 2499], ["Coffee", 31], ["Book", 60], ["Nike", 699]],需打印以下格式：略..
# 2.根据上面的products列表写一个循环，不断询问用户想买什么，用户选择一个商品编号，就把对应的商品添加的购物车里，用户最终输入q退出时，打印购买的商品列表。

products = [["iphone", "6888"], ["MacPro", "14800"], ["小米6", "2499"], ["Coffee", "31"], ["Book", "60"], ["Nike", "699"]]

print("-"*6+"\t"+"商品列表"+"\t"+"-"*6)
number = 0

for product in products:
    print(number, end="\t")
    number += 1
    for data in product:
        print(data, end="\t")
    print("")

'''
shoppingCart = []
goodNumber = input("请输入需要购买的商品编号：")
if goodNumber == "0":
    shoppingCart.append(products[0])




elif goodNumber == "q":
    print("-" * 6 + "\t" + "购物车" + "\t" + "-" * 6)
    print(shoppingCart)
else:
    shoppingCart.append(products[goodNumber])
'''
