import requests

data = {
    "kw": "dog"
}

url = "https://fanyi.baidu.com/sug"

resp = requests.post(url=url, data=data)

resp_json = resp.json()

print(resp.json())
