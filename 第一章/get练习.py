import requests

url = "https://www.sogou.com/web?query=周杰伦"

resp = requests.get(url=url)

# print(resp.text)

with open("sogou.html", mode="w", encoding="utf-8") as f:
    f.write(resp.text)