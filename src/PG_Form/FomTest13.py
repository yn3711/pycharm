##****************************************************************************************
##   TITLE   :
##   SYSTEM  :
##
##   PROJECT :
##   FILE-ID :  FomTst13
##
##   WRITE   :  99/99/99
##   UPDATE  :  99/99/99
##
##   REMRAKS : hhttps://qiita.com/yut-nagase/items/b55e7ab3c1dcc6544e5f
##****************************************************************************************
# -*- coding: utf-8 -*-
from flask import Flask, render_template

app = Flask(__name__)

##////////////////////////////////////////////////
##  Class       : FomTest13
##  Base        :
##  Note        :
##////////////////////////////////////////////////
class FomTst13(Flask):

    #def __init__(self):
    user_name1 = "田中　一郎"

    ##======================================================================================
    ##
    ## @Return:
    ## @Note:
    ##======================================================================================
    # メニューを表示
    @app.route("/")
    def menu():
        #user_name1 = "田中　一郎"
        return render_template("index13.html", user_name=FomTst13.user_name1)
    ##======================================================================================
    ##
    ## @Return:
    ## @Note:
    ##======================================================================================
    # マイページ
    @app.route("/mypage")
    def walk():
        user_name = "田中　一郎"
        menu_name = "マイページ"
        info = "会員ランク：A"
        return render_template("index13_01.html", menu_name=menu_name, user_name=user_name, info=info)

    ##======================================================================================
    ##
    ## @Return:
    ## @Note:
    ##======================================================================================
    # 購入履歴
    @app.route("/history")
    def attack():
        user_name = "田中　一郎"
        menu_name = " 購入履歴"
        info = "2018.11.01 iMac 120,000"
        return render_template("index13_01.html", menu_name=menu_name, user_name=user_name, info=info)

if __name__ == '__main__':
    app.debug = True
    app.run()