#函数的定义
'''
def printinfo():
    print("--------------------------")
    print("    人生苦短，我用Python    ")
    print("--------------------------")

#函数的调用
printinfo()
'''

#带参数的函数
'''
def add2Num(a,b):
    c = a + b
    print(c)

add2Num(11,22)
'''

#带返回值的函数
'''
def add2Num(a,b):
    return a+b      #通过reture来返回运算结果

result = add2Num(11,22)
print(result)
#print(add2Num(11,22))
'''

#返回多个值的函数
'''
def divid(a,b):
    shang = a//b
    yushu = a%b
    return shang,yushu      #多个返回值用逗号分割

sh,yu = divid(5,2)      #需要使用多个值来保存返回内容

print("商：%d，余数：%d"%(sh,yu))
'''

#课堂练习
#1.写一个打印一条横线的函数。（提示：横线是若干个"-"组成）
'''
def printlines():
    print("-"*15)

#printlines()

#2.写一个函数，可以通过输入的参数，打印出自定义行数的横线。（提示：调用上面的函数）

def printlines1(n):
    i = 0
    while i < n:
        printlines()
        i += 1
        
printlines1(3)
'''

#3.写一个函数求三个数的和
'''
def sum(a,b,c):
    return a+b+c
#print(sum(1,2,3))


#4.写一个函数求三个数的平均值（提示：调用上面的函数）
def average(a,b,c):
    ave = sum(a,b,c)/3
    return ave

print(average(1,2,3))
'''

#全局变量和局部变量
'''
def test1():
    a = 300     #局部变量
    print("test1------修改前：a= %d"%a)
    a = 100
    print("test1------修改后：a= %d" % a)

def test2():
    a = 500     #不同的函数可以定义相同的名字，彼此无关
    print("test2------a= %d" % a)

test1()
test2()
'''

'''
a = 100     #全局变量
def test1():
    print(a)

def test2():
    print(a)        #调用全局变量a

test1()
test2()
'''


#全局变量和局部变量相同名字
'''
a = 100
def test1():
    a = 300     #局部变量优先使用
    print("test1------修改前：a= %d"%a)
    a = 200
    print("test1------修改后：a= %d" % a)

def test2():
    print("test2------a= %d" % a)       #没有局部变量，默认使用全局变量

test1()
test2()
'''

#在函数中修改全局变量
a = 100     #全局变量
def test1():
    global a        #声明全局变量在函数中的标识符
    print("test1------修改前：a= %d"%a)
    a = 200
    print("test1------修改后：a= %d" % a)

def test2():
    print("test2------a= %d" % a)       #没有局部变量，默认使用全局变量

test1()
test2()




