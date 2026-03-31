##****************************************************************************************
##   TITLE   :
##   PROJECT :
##   REMRAKS : https://kazuhira-r.hatenablog.com/entry/2019/08/14/235805
##****************************************************************************************
# coding: utf-8
from flask import Flask
from flask_restful import Api, Resource

##////////////////////////////////////////////////
##  Class       : FomRestful
##  Base        :
##  Note        :
##////////////////////////////////////////////////
class FomRestful(Resource):

  app = Flask(__name__) #FlaskおよびApiのインスタンスを作成
  api = Api(app)

  ##======================================================================================
  ##
  ## @Parameter:
  ## @Return:
  ## @Note:
  ##======================================================================================
  def get(self):
      return {'message': 'Hello World'}

#class VariableRouting(Resource):  #localhost:5000/var/123456
  def get(self, id):
      return { 'id': id }

#FomRestful.api.add_resource(FomRestful, '/') #Resourceクラスを登録  第2引数が、ルーティングのパス
#FomRestful.api.add_resource(VariableRouting, '/var/<string:id>')
FomRestful.api.add_resource(FomRestful, '/var/<string:id>')

if __name__ == "__main__":
      FomRestful.app.run(debug=True)