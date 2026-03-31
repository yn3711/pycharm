##****************************************************************************************
##   TITLE   :
##   PROJECT :
##   REMRAKS : https://kazuhira-r.hatenablog.com/entry/2019/08/14/235805
##****************************************************************************************
# coding: utf-8
from flask import Flask, request
from flask_restful import Api, Resource, reqparse

##////////////////////////////////////////////////
##  Class       : FomRestful01
##  Base        :
##  Note        :
##////////////////////////////////////////////////
class FomRestful01(Resource):

  app = Flask(__name__) #FlaskおよびApiのインスタンスを作成
  api = Api(app)

  parser = reqparse.RequestParser()
  ##======================================================================================
  ##
  ## @Parameter:
  ## @Return:
  ## @Note:
  ##======================================================================================
  def get(self):
      query_string = request.query_string
      param = request.args.get('param')

      return {
          'query_string': query_string.decode('utf-8'),
          'param': param
      }


class PostResource(Resource):
    def post(self):
        json = request.get_json(force=True)
        return {'json_request': json}

FomRestful01.api.add_resource(FomRestful01, '/get')
FomRestful01.api.add_resource(PostResource, '/post')

if __name__ == "__main__":
      FomRestful01.app.run(debug=True)