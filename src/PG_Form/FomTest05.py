##****************************************************************************************
##   TITLE   :
##   SYSTEM  :
##
##   PROJECT :
##   FILE-ID :  FomTest05
##
##   WRITE   :  99/99/99
##   UPDATE  :  99/99/99
##
##   REMRAKS :https://tanuhack.com/flask-client2server/
##****************************************************************************************
# -*- coding: utf-8 -*-
from flask import Flask, render_template, request

##////////////////////////////////////////////////
##  Class       : FomTest05
##  Base        :
##  Note        :
##////////////////////////////////////////////////
class FomTst05:
  app = Flask(__name__)

  ##======================================================================================
  ##  'GET', 'POST'
  ## @Return:
  ## @Note:
  ##======================================================================================
  # getのときの処理
  @app.route('/', methods=['GET'])
  def get():
      return render_template('index05.html', \
		                       title = 'Form Sample(get)', \
		                       message = '名前を入力して下さい。')
  ##======================================================================================
  ##  'GET', 'POST'
  ## @Return:
  ## @Note:
  ##======================================================================================
  # postのときの処理
  @app.route('/', methods=['POST'])
  def post():
      name = request.form['name']
      return render_template('index05.html', \
		                        title = 'Form Sample(post)', \
		                        message = 'こんにちは、{}さん'.format(name))

  if __name__ == '__main__':
      app.run()