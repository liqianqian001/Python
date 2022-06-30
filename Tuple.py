'''
tup1 = ()    #创建空的元组 <class 'tuple'>
print(type(tup1))

tup2 = (50)   #<class 'int'> 这样定义的类型是int，不是元组
print(type(tup2))

tup3 = (50,)    #<class 'tuple'>当只有一个数值时，加个逗号隔开，类型是元组
print(type(tup3))

tup4 = (50,60,70)   #<class 'tuple'>
print(type(tup4))
'''

'''
tup1 = ("adc","def",2000,2020,444,555,666)

print((tup1[0]))
print(tup1[-1])     #访问最后一个元素
print(tup1[1:5])    #左闭右开
'''
'''
#增 (连接)
tup1 = (12,34,56)
tup2 = ("adc","xyz")

tup = tup1 + tup2
print(tup)
'''

#删
tup1 = (12,34,56)
del tup1        #删除了整个元组变量
print("删除后：")
print(tup1)


#改
#up1 = (12,34,56)

#tup1[0] = 100    #报错，不允许修改

#查