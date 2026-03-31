##****************************************************************************************
##   TITLE   :
##   SYSTEM  :
##
##   PROJECT :
##   FILE-ID :  FomTest03
##
##   WRITE   :  99/99/99
##   UPDATE  :  99/99/99
##
##   REMRAKS :https://start-python.hateblo.jp/entry/2020/01/25/090000
##****************************************************************************************
from flask import Flask, render_template, request

app = Flask(__name__)

##////////////////////////////////////////////////
##  Class       : FomTest03
##  Base        :
##  Note        :
##////////////////////////////////////////////////
class FomTst03:

  #app = Flask(__name__)

  ##======================================================================================
  ##
  ## @Return:
  ## @Note:
  ##======================================================================================
  '''
  @app.route('/')
  def index():
      return render_template('index03.html')
'''
  @app.route('/')
  def index():
      return render_template('index03_1.html')

  ##======================================================================================
  ##
  ## @Return:
  ## @Note:
  ##======================================================================================
  @app.route('/test', methods=['GET', 'POST'])
  def test():
      if request.method == 'GET':
          res = request.args.get('get_button')
      elif request.method == 'POST':
          res = render_template('index03.html')
      return res


'''
  if __name__ == "__main__":
      app.run(debug=True)
'''

if __name__ == "__main__":
   app.run(debug=True)