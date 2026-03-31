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
##   REMRAKS : https://qiita.com/yaaamaaaguuu/items/486968e3b566f8340a9e
##             http://localhost:5000/hello/
##****************************************************************************************
# -*- coding: utf-8 -*-
from flask import Flask
from flask_classy import FlaskView

app = Flask(__name__)

##////////////////////////////////////////////////
##  Class       :
##  Base        :
##  Note        :
##////////////////////////////////////////////////
class HelloView(FlaskView):

    name = "hello world"
    ##======================================================================================
    ##
    ## @Return:
    ## @Note:
    ##======================================================================================
    def index(self):
        return self.name

HelloView.register(app)

if __name__ == '__main__':
        app.run()