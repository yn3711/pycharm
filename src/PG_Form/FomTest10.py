##****************************************************************************************
##   TITLE   :
##   SYSTEM  :
##
##   PROJECT :
##   FILE-ID :  FomTst10
##
##   WRITE   :  99/99/99
##   UPDATE  :  99/99/99
##
##   REMRAKS :https://tanuhack.com/flask-client2server/
##****************************************************************************************
# -*- coding: utf-8 -*-
from flask import Flask
from flask import request
from flask import render_template
import time


##////////////////////////////////////////////////
##  Class       : FomTest10
##  Base        :
##  Note        :
##////////////////////////////////////////////////
class FomTst10:
    app = Flask(__name__)

    ##======================================================================================
    ##  'GET', 'POST'
    ## @Return:
    ## @Note:
    ##======================================================================================
    def long_load(typeback):
       time.sleep(5) #just simulating the waiting period
       return "You typed: %s" % typeback

    ##======================================================================================
    ##  'GET', 'POST'
    ## @Return:
    ## @Note:
    ##======================================================================================
    @app.route('/')
    def home():
       return render_template("index10.html")

    @app.route('/', methods=['POST'])
    def form(display=None):
      query = request.form['anything']
      outcome = long_load(query)
      return render_template("done.html", display=outcome)

    if __name__ == '__main__':
      app.debug = True
      app.run()