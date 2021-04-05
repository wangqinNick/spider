import requests
import re

url = "https://movie.douban.com/top250"

headers = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"
}

resp = requests.get(url=url, headers=headers)
text_s = resp.text

# print(text_s)

obj = re.compile(r'<li>.*?<span class="title">(?P<name>.*?)</span>.*?'
                 r'<div class="bd">.*?<br>.*?(?P<year>\d{4}).*?</p>.*?'
                 r'<div class="star">.*?<span class="rating_num" property="v:average">(?P<rating>.*?)</span>.*?'
                 r'<span>(?P<num_review>\d*)人评价</span>', flags=re.S)

result = obj.finditer(string=text_s)

movie_info = {}
for i in result:
    name = i.group("name")
    year = i.group("year")
    rating = i.group("rating")
    num_review = i.group("num_review")

    dic = i.groupdict()

print(dic)
