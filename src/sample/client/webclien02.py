#https://itsakura.com/python-http
#POSTで上記サーバにアクセスするコードのサンプルです。

# coding: utf-8
import requests

url = 'http://localhost:8765'

test1 = {
    "color1": "a",
    "color2": "c"
}

##response = requests.post(url, test1)
response = requests.post(url, "")

print(response.text)