#字典的定义
'''
info = {"name":"吴彦祖","age":18}
'''
#字典的访问
'''
print(info["name"])
print(info["age"])
'''

#访问不存在的健
'''
#print(info["gender"])          #直接访问，会报错

print(info.get("gender"))       #使用get方法，没有找到对应的键，默认返回None

print(info.get("gender","m"))       #没找到的时候，可以设定默认值
print(info.get("age","20"))     #能找到age，不使用默认值
'''

#增
'''
info = {"name":"吴彦祖","age":18}
newID = input("请输入新的学号")
info["id"] = newID
print(info["id"])
'''
#删
#【del】
'''
info = {"name":"吴彦祖","age":18}
print("删除前：%s"%info["name"])
del info["name"]
'''
#print("删除后：%s"%info["name"])    #删除了指定键值对后，再次访问会报错

'''
info = {"name":"吴彦祖","age":18}
print("删除前：%s"%info)

del info
print("删除后：%s"%info)    #删除字典后，再访问报错
'''

#【clear】  清空
'''
info = {"name":"吴彦祖","age":18}

print("清空前：%s"%info)
info.clear()
print("清空后：%s"%info)        #清空后：{}
'''

#改
'''
info = {"name":"吴彦祖","age":18}

info["age"] = 20
print(info["age"])
'''

#查  【遍历】

info = {"id":1,"name":"吴彦祖","age":18}
'''
print(info.keys())      #得到所有的键（列表）

print(info.values())      #得到所有的值（列表）

print(info.items())      #得到所有的项（列表）,每个键值对是一个元组
'''

#遍历所有的键
'''
for key in info.keys():
    print(key)
'''

#遍历所有的值
'''
for value in info.values():
    print(value)
'''

#遍历所有的键值对
'''
for key,value in info.items():
    print("key=%s,value=%s"%(key,value))
'''

#使用枚举函数，同事拿到列表中的下标和元素内容
myList = ["a","b","c","d"]
for i,x in enumerate(myList):
    print(i,x)










