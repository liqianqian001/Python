# for..in..循环语句
'''
for i in range(5):   # 从0开始，到4结束
    print(i)
'''

'''
for i in range(0, 10, 3):   # 从0开始，到10结束，步进值加3（每次+3）
    print(i)
'''

'''
for i in range(-10, -100, -30):
    print(i)
'''

'''
name = "jiaxing"
for x in name:
    print(x, end="\t")
'''

'''
a = ["aa", "bb", "cc", "dd"]
for i in range(len(a)):
    print(i, a[i])
'''
# while循环
'''
i = 0
while i < 5:
    print("当前是第%d次循环"%(i+1))
    print("i=%d"%i)
    i += 1
'''
# 练习：0-100求和
'''
a = 0    # 用for..in循环写
for i in range(1, 101):
    a += i
    # print(i)
print("0到100求和结果为%d"%a)
'''
'''
a = 100    # 用while语句写
sum = 0
counter = 1
while counter <= a:
    sum += counter
    counter += 1
print("0到%d求和结果为: %d"%(a, sum))
'''
# else在whlie循环语句的使用
'''
count = 0
while count < 5:
    print(count, "小于5")
    count += 1
else:
    print(count, "大于或等于5")
'''
# break和continue循环（了解一下）
'''
i = 0
while i < 5:
    i += 1
    print("-"*30)
    if i == 5:
        break    # break结束掉整个循环
    print(i)
'''
'''
i = 0
while i < 10:
    i += 1
    print("-"*30)
    if i == 5:
        continue    # continue：结束本次循环（本次循环continue之后的语句都不再执行）
    print(i)
'''

# 用for循环和while循环，打印九九乘法表
'''
n = 9
z = 1
for x in range(1, n+1):    # 用for循环打印
    for y in range(1, n+1):
        z = x * y
        if x > y:
            print("%d*%d=%d" % (x, y, z), end="\t")
        elif x == y:
            print("%d*%d=%d" % (x, y, z))
            break
'''
n = 9
x = 1
y = 1
z = 1
while x <= 9:
    while y <= 9:
        z = x * y
        if x > y:
            print("%d*%d=%d" % (x, y, z), end="\t")
        elif x == y:
            print("%d*%d=%d" % (x, y, z))
            y = 1
            break
        y += 1
    x += 1
