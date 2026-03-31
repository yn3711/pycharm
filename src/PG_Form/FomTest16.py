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
##   REMRAKS : https://start-python.hateblo.jp/entry/2020/03/15/090000
##             https://rfs.jp/sb/javascript/02js/browser_object.html#Navigator
##
##****************************************************************************************
# -*- coding: utf-8 -*-
from flask import Flask, render_template
from flask_classy import FlaskView

app = Flask(__name__)

##////////////////////////////////////////////////
##  Class       :
##  Base        :
##  Note        :
##////////////////////////////////////////////////
class FomTest16(FlaskView):

    ##======================================================================================
    ##
    ## @Return:
    ## @Note:
    ##======================================================================================
    @app.route('/')
    def index():
        return render_template('index16.html')

if __name__ == '__main__':
    app.run(debug=True)