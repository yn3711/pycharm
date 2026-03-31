##****************************************************************************************
##   TITLE   :
##   SYSTEM  :
##
##   PROJECT :
##   FILE-ID :  FomTst08
##
##   WRITE   :  99/99/99
##   UPDATE  :  99/99/99
##
##   REMRAKS :https://tanuhack.com/flask-client2server/
##****************************************************************************************
# -*- coding: utf-8 -*-
from flask import Flask, render_template, request


##////////////////////////////////////////////////
##  Class       : FomTest08
##  Base        :
##  Note        :
##////////////////////////////////////////////////
class FomTst08:

  app = Flask(__name__)

  ##======================================================================================
  ##  'GET', 'POST'
  ## @Return:
  ## @Note:
  ##======================================================================================
  @app.route('/', methods=['GET'])
  def get():
	return render_template('index08.html', \
		title = 'Form Sample(get)', \
		message = '何のお肉が好きですか？')

  ##======================================================================================
  ##  'GET', 'POST'
  ## @Return:
  ## @Note:
  ##======================================================================================
  @app.route('/', methods=['POST'])
  def post():
	name = request.form.get('sel')
	return render_template('index08.html', \
		title = 'Form Sample(post)', \
		message = '{}の肉がお好きなんですね！'.format(name))

  if __name__ == '__main__':
	app.run()