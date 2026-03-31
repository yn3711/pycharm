#https://itsakura.com/python-http

# coding: utf-8
import requests

url = 'http://localhost:8765'

response = requests.get(url)
print(response.text)