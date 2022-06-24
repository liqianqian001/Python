#namelist = []   # 定义一个空列表
namelist = ["小张", "小王", "小李" ]
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
