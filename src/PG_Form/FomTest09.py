##****************************************************************************************
##   TITLE   :
##   SYSTEM  :
##
##   PROJECT :
##   FILE-ID :  FomTst
##
##   WRITE   :  99/99/99
##   UPDATE  :  99/99/99
##
##   REMRAKS :https://tanuhack.com/flask-client2server/
##****************************************************************************************
# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os

##////////////////////////////////////////////////
##  Class       : FomTest
##  Base        :
##  Note        :
##////////////////////////////////////////////////
class FomTst09:

  app = Flask(__name__)

  # ファイル容量上限 : 1MB
  app.config['MAX_CONTENT_LENGTH'] = 1 * 1024 * 1024

  ##======================================================================================
  ##  'GET', 'POST'
  ## @Return:
  ## @Note:
  ##======================================================================================
  @app.route('/', methods=['GET'])
  def get():
	  return render_template('index09.html', \
						   title='Form Sample(get)', \
						   message='画像を選択して下さい。', \
						   flag=False)

  ##======================================================================================
  ##  'GET', 'POST'
  ## @Return:
  ## @Note:
  ##======================================================================================
  @app.route('/', methods=['POST'])
  def post():
	  # ファイルのリクエストパラメータを取得
	  f = request.files.get('image')

	  # ファイル名を取得
	  filename = secure_filename(f.filename)

	  # ファイルを保存するディレクトリを指定
	  filepath = 'static/image/' + filename

	  # ファイルを保存する
	  f.save(filepath)

	  return render_template('index09.html', \
						   title='Form Sample(post)', \
						   message='アップロードされた画像({})'.format(filename), \
						   flag=True, \
						   image_name=filename, \
						   image_url=filepath)


  if __name__ == '__main__':
	  app.run()