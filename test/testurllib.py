# -*- codeing = utf-8 -*-
# @Time : 2022-01-01 9:11
# @Author : 齐物逍遥游
# @File : testurllib.py
# @Software: PyCharm


import urllib.request

# #获取一个get请求
# response = urllib.request.urlopen("http://www.baidu.com")
# print(response.read().decode("utf-8"))  #对获取到的网页源码进行utf-8解码

#获取一个post请求

# import urllib.parse
# data = bytes(urllib.parse.urlencode({"hello":"world"}),encoding="utf-8")
# response = urllib.request.urlopen("http://httpbin.org/post",data= data)
# print(response.read().decode("utf-8"))

# #超时处理
# try:
#     response = urllib.request.urlopen("http://httpbin.org/get",timeout=0.01)
#     print(response.read().decode("utf-8"))
# except urllib.error.URLError as e:
#     print("time out!")

# response = urllib.request.urlopen("http://www.baidu.com")
#
# print(response.getheaders())

#url = "https://www.douban.com"
# url = "http://httpbin.org/post"
# headers = {
# "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
# }
# data = bytes(urllib.parse.urlencode({"name":"song"}),encoding="utf-8")
# req = urllib.request.Request(url=url,data=data,headers=headers,method="POST")
# response = urllib.request.urlopen(req)
# print(response.read().decode("utf-8"))

url = "https://www.douban.com"
headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
}
req = urllib.request.Request(url=url,headers=headers)
response = urllib.request.urlopen(req)
print(response.read().decode("utf-8"))


#uban.com%2F%22%5D; _pk_ses.100001.4cf6=*; __utma=223695111.717513958.1605487505.1641125023.1641361964.64; __utmb=223695111.0.10.1641361964; __utmz=223695111.1641361964.64.36.utmcsr=accounts.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; push_noty_num=0; push_doumail_num=0; __utmv=30149280.22558; __utmb=30149280.5.10.1641361694; dbcl2="225585964:nzNvs8w+Wd8"; ck=jbRy; _pk_id.100001.4cf6=ea3d493156bf90ec.1605487505.64.1641366108.1641126221.; __utmc=30149280; __utmc=223695111