# -*- coding: utf-8 -*-
'''
BeautifulSoup4将复杂HTML文档转换成一个复杂的树形结构，每个节点都是Python对象，所有对象可以归纳为4种：
- Tag
- Navigablestring
- BeautifulSoup
- Comment
'''
import re

from bs4 import BeautifulSoup

file = open("./baidu.html","rb")        # .就是当前文件夹，baidu.html是一个网页文件
html = file.read()
bs = BeautifulSoup(html,"html.parser")      #通过html.parser解析器，解析html，形成一个文件树

# 1.Tag 标签及其内容；拿到它所找到的第一个内容
print(bs.title)     #把文件中的title拿出来
print(type(bs.title))

# 2.Navigablestring 标签里的内容（字符串）
print(bs.title.string)
print(type(bs.title.string))

# 快速拿到标签里的所有属性，以键值对的方式
print(bs.a.attrs)

# 3.BeautifulSoup  表示整个文档
print(type(bs))
print(bs)
print(bs.name)

# 4.Comment  是一个特殊的NavigablesSring，输出的内容不包含注释符号
print(bs.a.string)
print(type(bs.a.string))

#----------------分割线------------------

#文档的遍历
print(bs.head.contents)
print(bs.head.contents[1])



#文档的搜索
#(1)find_all
#字符串过滤：会查找与字符串完全匹配的内容
# t_list = bs.find_all("a")

import re
#正则表达式搜索：search（）方法来匹配内容
#t_list = bs.find_all(re.compile("a"))
# print(t_list)

#方法：传入一个函数（方法），根据函数的要求来搜索(了解)
# def name_is_exist(tag):
#     return tag.has_attr("name")
#
# t_list = bs.find_all(name_is_exist)
#
# for item in t_list:
#     print(item)

#2.kwargs 参数
# t_list = bs.find_all(id="head")
# t_list = bs.find_all(href="http://news.baidu.com")
# t_list = bs.find_all(class_=True)

# for item in t_list:
#     print(item)

#3.text参数
#t_list = bs.find_all(text="hao123")
#t_list = bs.find_all(text=["hao123","地图","贴吧"])
#t_list = bs.find_all(text=re.compile("\d"))     #应用正则表达式来查找包含特定文本的内容（标签里的字符串）

#4.limit参数
# t_list = bs.find_all("a",limit=3)       #限定获取多少个
# for item in t_list:
#     print(item)

#css选择器
# t_list = bs.select('title')     #通过标签来查找
# t_list = bs.select(".mnav")     #通过类名来查找
# t_list = bs.select("#u1")       #通过id来查找
# t_list = bs.select("a[class='bri']")     #通过属性来查找
# t_list = bs.select("head > title")  #通过子标签来查找

t_list = bs.select(".mnav ~ .bri")
print(t_list[0].get_text())

# for item in t_list:
#     print(item)






























