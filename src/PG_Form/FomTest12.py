##****************************************************************************************
##   TITLE   :
##   SYSTEM  :
##
##   PROJECT :
##   FILE-ID :  FomTst12
##
##   WRITE   :  99/99/99
##   UPDATE  :  99/99/99
##
##   REMRAKS : https://tanuhack.com/flask-jinja2-import/
##****************************************************************************************
# -*- coding: utf-8 -*-
from flask import Flask, render_template

app = Flask(__name__)

##////////////////////////////////////////////////
##  Class       : FomTest12
##  Base        :
##  Note        :
##////////////////////////////////////////////////
class FomTst12:

    #app = Flask(__name__)

    ##======================================================================================
    ## POST
    ## @Return:
    ## @Note:
    ##======================================================================================
    @app.route('/')
    def index():
        return render_template('index12.html')

'''
    # => arr1 ['1', '2', '3', '4', '5']
    if __name__ == '__main__':
      app.debug = True
      app.run()
'''

if __name__ == '__main__':
    app.debug = True
    app.run()