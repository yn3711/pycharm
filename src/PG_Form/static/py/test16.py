##****************************************************************************************
##   TITLE   :
##   SYSTEM  :
##
##   PROJECT :
##   FILE-ID :
##
##   WRITE   :  99/99/99
##   UPDATE  :  99/99/99
##
##   REMRAKS :
##
##****************************************************************************************
# -*- coding: utf-8 -*-
from browser import document, alert

alert("URL：" + document.location.href)
alert("ホスト名：" + document.location.hostname)
alert("クエリ：" + document.location.search)
alert("パス：" + document.location.pathname)

def echo(event):

    ##// URLを取得、設定します
    #alert("URL：" + location.href)

    alert(document["text1"].value)

    ##// URLを取得、設定します
    ##alert("URL：" + location.href)
    ##// URLのホスト名を取得、設定します
    #console.log("ホスト名：" + location.hostname)
    ##// URLの?以降を取得、設定します
    #console.log("クエリ：" + location.search)
    #console.log("URLの以降：" + location.hash )
    ##// パスを取得、設定します
    #console.log("パス：" + location.pathname)


document["btn1"].bind("click", echo)