##****************************************************************************************
##   TITLE   :
##   PROJECT :
##   REMRAKS :
##****************************************************************************************
# coding: utf-8
from flask import Flask, jsonify, abort, request

##////////////////////////////////////////////////
##  Class       : FomJson
##  Base        :
##  Note        :
##////////////////////////////////////////////////
class FomJson:

  app = Flask(__name__)

  app.config['JSON_AS_ASCII'] = False # < -- これ

  tasks = [
      {
          'id': 1,
          'title': '日用品を買ってくる',
          'description': 'ミルク、チーズ、ピザ、フルーツ',
          'done': False
      },
      {
          'id': 2,
          'title': 'Python の勉強',
          'description': 'Python で Restful api を作る',
          'done': False
      }
  ]

  ##======================================================================================
  ##
  ## @Parameter:
  ## @Return:
  ## @Note:
  ##======================================================================================
  @app.route('/')
  def index():
      return 'Hello World!日本語'

  @app.route('/todo/api/v1.0/tasks', methods=['GET'])
  def get_tasks():
      return jsonify({'tasks': tasks})

  if __name__ == "__main__":
      app.run(debug=True)