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

def echo(event):
    alert(document["text1"].value)

document["btn1"].bind("click", echo)