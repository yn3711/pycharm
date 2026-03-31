##****************************************************************************************
##   TITLE   :
##   SYSTEM  :
##
##   PROJECT :
##   FILE-ID :  FomTest01
##
##   WRITE   :  99/99/99
##   UPDATE  :  99/99/99
##
##   REMRAKS :https://teratail.com/questions/311004
##****************************************************************************************
from flask import Flask, render_template, request

app = Flask(__name__)

##////////////////////////////////////////////////
##  Class       : FomTest01
##  Base        :
##  Note        :
##////////////////////////////////////////////////
class FomTest01(object):

  #app = Flask(__name__)

  ##======================================================================================
  ##
  ## @Return:
  ## @Note:
  ##======================================================================================
  @app.route("/", methods=["GET", "POST"])
  def index():
    if request.method == 'POST':
        if request.form['send'] == 'aaa':
            m = '12345'
            return render_template('index.html', message=m)

        if request.form['send'] == 'bbb':
            m = '67890'
            return render_template('index.html', message=m)

        if request.form['send'] == 'ccc':
            m = '1234567890'
            return render_template('index.html', message=m)
    else:
        return render_template('index.html')

#  if __name__ == "__main__":
#    app.run(host = '127.0.0.1', port = '5000')
if __name__ == "__main__":
  app.run(host = '127.0.0.1', port = '5000')