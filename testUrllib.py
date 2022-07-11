import urllib.request

#获取一个get请求
# response = urllib.request.urlopen("http://www.baidu.com")
# print(response.read().decode('utf-8'))      #对获取到的网页源码进行utf-8解码

#获取一个post请求

# import urllib.parse
# data = bytes(urllib.parse.urlencode({"hello":"world"}),encoding="utf-8")
# response = urllib.request.urlopen("http://httpbin.org/post",data=data)
# print(response.read().decode("utf-8"))


#超时处理
# try:
#     response = urllib.request.urlopen("http://httpbin.org/get",timeout=0.01)       #超时0.01s就报错处理
#     print(response.read().decode("utf-8"))
# except urllib.error.URLError as e:
#     print("time out!")


# response = urllib.request.urlopen("http://www.baidu.com")
# # print(response.status)
# print(response.getheader("Server"))


# url = "http://httpbin.org/post"
# headers = {
# "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
# }
# data = bytes(urllib.parse.urlencode({'name':'eric'}),encoding="utf-8")
# req = urllib.request.Request(url=url,data=data,headers=headers,method="POST")
# response = urllib.request.urlopen(req)
# print(response.read().decode("utf-8"))


#全局取消证书验证（自己百度的两行～
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

#后续真正用到的代码！！
url = "https://www.douban.com"
headers = {                     #把自己伪装成一个正常用户（从网页header找到的用户代理信息）
"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
}
req = urllib.request.Request(url=url,headers=headers)       #封装req对象
response = urllib.request.urlopen(req)      #使用封装好的req对象访问网页
print(response.read().decode("utf-8"))      #以utf-8的方式解析






