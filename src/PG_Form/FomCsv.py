##****************************************************************************************
##   TITLE   :
##   PROJECT :
##   REMRAKS :
##****************************************************************************************
from flask import Flask, Response

##////////////////////////////////////////////////
##  Class       : FomCsv
##  Base        :
##  Note        :
##////////////////////////////////////////////////
class FomCsv:

  app = Flask(__name__)

  ##======================================================================================
  ##
  ## @Parameter:
  ## @Return:
  ## @Note:
  ##======================================================================================
  @app.route("/")
  def hello():
    return '''
        <html><body>
        Hello. <a href="/getPlotCSV">Click me.</a>
        </body></html>
        '''
  ##======================================================================================
  ##
  ## @Parameter:
  ## @Return:
  ## @Note:
  ##======================================================================================
  @app.route("/getPlotCSV")
  def getPlotCSV():
    # with open("outputs/Adjacency.csv") as fp:
    #     csv = fp.read()
    csv = '1,2,3\n4,5,6\n'
    return Response(
        csv,
        mimetype="text/csv",
        headers={"Content-disposition":
                 "attachment; filename=myplot.csv"})

  # サーバーを起動
  if __name__ == "__main__":
    app.run(debug=True)