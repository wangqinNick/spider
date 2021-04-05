import re

s = "我的电话是10086， 她的电话是10010"

lst = re.findall(r"\d+", s)

it = re.finditer(r"\d+", s)

obj = re.compile(r"\d+")

itr = obj.finditer(s)
for i in itr:
    print(i.group())
