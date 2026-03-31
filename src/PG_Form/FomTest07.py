##****************************************************************************************
##   TITLE   :
##   SYSTEM  :
##
##   PROJECT :
##   FILE-ID :  FomTst07
##
##   WRITE   :  99/99/99
##   UPDATE  :  99/99/99
##
##   REMRAKS :https://tanuhack.com/flask-client2server/
##****************************************************************************************
# -*- coding: utf-8 -*-
from flask import Flask, render_template, request

##////////////////////////////////////////////////
##  Class       : FomTest07
##  Base        :
##  Note        :
##////////////////////////////////////////////////
class FomTst07:

  app = Flask(__name__)

  ##======================================================================================
  ## GET
  ## @Return:
  ## @Note:
  ##======================================================================================
  @app.route('/', methods=['GET'])
  def get():
	  return render_template('index07.html', \
		title = 'Form Sample(get)', \
		message = '何のお肉が好きですか？')

  ##======================================================================================
  ##  POST
  ## @Return:
  ## @Note:
  ##======================================================================================
  @app.route('/', methods=['POST'])
  def post():
	  name = request.form.getlist('checkbox')
	  return render_template('index07.html', \
		title = 'Form Sample(post)', \
		message = '{}の肉がお好きなんですね！'.format('と'.join(name)))

  if __name__ == '__main__':
	  app.run()