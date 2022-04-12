# -*- codeing = utf-8 -*-
# @Time : 2022-01-02 8:50
# @Author : 齐物逍遥游
# @File : testBS4.py
# @Software: PyCharm


from bs4 import BeautifulSoup

file = open("./baidu.html","rb")
html = file.read()
bs = BeautifulSoup(html,"html.parser")    #bs是解析对象，用parser进行解析html


#1.Tag  标签及其内容；拿到它所找到的第一个内容，比如<title>
# print(bs.title)   #打印结果：<title>百度一下，你就知道 </title>

#2. NavigableString   标签里的内容（字符串）
# print(bs.title.string)  #打印结果：百度一下，你就知道

#3. Beautifulsoup  表示整个文档
# print(bs)   #打印结果：以文本形式打印整个文档

#4.Comment   是一个特殊的NavigableString，输出的内容不包含注释符号
# print(bs.a.string)    #打印结果：新闻

#--------------------------------------------

#文档的遍历

#print(bs.head.contents)



#文档的搜索

#一、find_all

#1.字符串过滤：会查找与字符串完全匹配的标签
#t_list = bs.find_all("a")   #查询所有带有“a"标签的内容，放入列表之中

#2.正则表达式搜索：适用search()方法来匹配内容
import re
# t_list = bs.find_all(re.compile("a"))       #找到所有正则表达式能匹配出来带“a”的标签

#3.方法：传入一个函数（方法），根据函数的要求来搜索  （了解掌握，功能强大，可自定义内容匹配内容）
# def name_is_exists(tag):
#     return tag.has_attr("name")
# t_list = bs.find_all(name_is_exists)
# #上述函数的意思大致是：定义一个函数name_is_exists,返回标签的内容中含有“name”的标签，找出这些标签
# for item in t_list:
#     print(item)   #可以分行打印返回的标签


#二、kwargs   参数

#t_list = bs.find_all(id="head")

# t_list = bs.find_all(class_=True)



#三、text参数   文本

#t_list = bs.find_all(text = re.compile("\d"))  #应用正则表达式来查找包含特定文本的内容（标签里的字符串）

#四、limit参数  限定获取的数量

# t_list = bs.find_all("a",limit=3)   #限定获取3个
#
# for item in t_list:
#     print(item)


#CSS选择器

#t_list = bs.select("title")  #通过标签来查找

# t_list = bs.select(".mnav")  #通过类名来查找

# t_list = bs.select("#u1")    #通过id来查找

# t_list = bs.select("a[class='bri']")  #通过属性来查找

# t_list = bs.select("head > title")  #通过子标签来查找

t_list = bs.select(".mnav ~ .bri")   #通过兄弟节点标签来查找
print(t_list[0].get_text())

# for item in t_list:
#     print(item)