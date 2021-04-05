import requests
import re

domain = "https://www.dy2018.com"

headers = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"
}

# 去掉安全验证
resp = requests.get(url=domain, headers=headers)

# 乱码问题，解码用默认utf-8，错了
# 制定字符集 为gb2312 （在网页源码上找到）
resp.encoding = 'gb2312'
resp_text = resp.text

# print(resp_text)

# 定位 "2020必看热片"
pattern1 = re.compile(r'.*?2020必看热片.*?<ul>(?P<block>.*?)</ul>', re.S)

pattern2 = re.compile(r"<li><a href='(?P<child>.*?)'.*?title.*?>"
                      r"(?P<title>.*?)</a><span>")

pattern3 = re.compile(r'<div class="title_all"><h1>(?P<title>.*?)</h1></div>.*?'
                      r'<td style="WORD-WRAP: break-word" bgcolor="#fdfddf"><a href="(?P<download>.*?)</a>', re.S)

result = pattern1.match(resp_text)

block_text = result.group("block")

result = pattern2.finditer(block_text)

for i in result:
    child = i.group("child")
    extension = domain + child
    # print(extension)

    movie_resp = requests.get(extension)
    movie_resp.encoding = 'gbk'
    movie_info = pattern3.search(movie_resp.text)
    print(movie_info.group("title"), movie_info.group("download"))






