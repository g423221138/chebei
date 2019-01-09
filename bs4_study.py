#bs4官方文档学习

#例子文档
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

#实例编写
from bs4 import BeautifulSoup
import re

soup = BeautifulSoup(html_doc, 'html.parser')

#让数据按照标准格式输出
print(soup.prettify())

#几个简单地浏览结构化数据的方法
print(soup.title)

print(soup.title.name)

print(soup.title.string)

print(soup.title.parent.name)

print(soup.p)

print(soup.a)

print(soup.find_all('a'))

print(soup.find(id="link3"))

#从文档中获取所有文字内容:
print(soup.get_text())

#输出所有字符串
for string in soup.strings:
    print(repr(string))

#去除多余空白字符串
for string in soup.stripped_strings:
    print(repr(string))

#find_all用法举例
#从文档中找到所有<a>标签的链接:
for link in soup.find_all('a'):
    print(link.get('href'))

#查找匹配标签及属性
print(soup.find_all("p", "title"))

#查找特定id属性
print(soup.find_all(id = "link2"))

#可正则查找href属性
print(soup.find_all(href = re.compile("elsie")))

#正则可模糊查找匹配字符串
print(soup.find_all(string = re.compile("sisters")))

#同时查找匹配多个字符串
print(soup.find_all(string = ["Tillie", "Elsie", "Lacie"]))

#limit参数，限制输出结果数量
print(soup.find_all("a", limit = 2))