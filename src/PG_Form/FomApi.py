##****************************************************************************************
##   TITLE   :
##   PROJECT :
##   REMRAKS : https://www.sukerou.com/2018/11/python3flask-rest-api.html
##             「http://127.0.0.1:5000/user/U001」を入力
##****************************************************************************************
# coding: utf-8
from flask import Flask, jsonify, abort, request

app = Flask(__name__)

##////////////////////////////////////////////////
##  Class       : FomApi
##  Base        :
##  Note        :
##////////////////////////////////////////////////
class FomApi:

  #app = Flask(__name__)

  # テストデータ
  users = [
    {"id": "U001", "name": "ユーザ太郎", "age": 27},
    {"id": "U002", "name": "ユーザ二郎", "age": 20},
    {"id": "U003", "name": "ユーザ三郎", "age": 10}
  ]

  ##======================================================================================
  ##
  ## @Parameter:
  ## @Return:
  ## @Note:
  ##======================================================================================
  @app.route('/user/<string:id>', methods=['GET'])
  def findUser(id):
    """
    ユーザを１件取得する
    """
    result = [n for n in FomApi.users if n["id"] == id] #users

    if len(result) >= 1:
        # ユーザ情報を返却
        return jsonify(result)
    else:
        # 存在しないユーザIDが指定された
        abort(404)


  ##======================================================================================
  ##
  ## @Parameter:
  ## @Return:
  ## @Note:
  ##======================================================================================
  @app.route('/user/', methods=['POST'])
  def createUser():
    """
    ユーザを登録する
    """
    # ユーザを追加
    data = {
        "id": request.form["id"],
        "name": request.form["name"],
        "age": int(request.form["age"])
    }
    FomApi.users.append(data)#users

    # 正常に登録できたので、HTTP status=204(NO CONTENT)を返す
    return '', 204


  ##======================================================================================
  ##
  ## @Parameter:
  ## @Return:
  ## @Note:
  ##======================================================================================
  @app.route('/user/', methods=['PUT'])
  def updateUser():
    """
    ユーザを更新する
    """
    id = request.form["id"]
    lst = [val for val in FomApi.users if val["id"] == id]#users

    if len(lst) >= 1:
        lst[0]["name"] = request.form["name"]
        lst[0]["age"] = int(request.form["age"])
    else:
        # 存在しないユーザIDが指定された場合
        abort(404)

    # 正常に更新できたので、HTTP status=204(NO CONTENT)を返す
    return '', 204


  ##======================================================================================
  ##
  ## @Parameter:
  ## @Return:
  ## @Note:
  ##======================================================================================
  @app.route('/user/<string:id>', methods=['DELETE'])
  def deleteUser(id):
    """
    ユーザを削除する
    """
    lst = [i for i, val in enumerate(FomApi.users) if val["id"] == id]#users
    for index in lst:
        del FomApi.users[index]#users

    if len(lst) >= 1:
        # ユーザの削除を行った場合、HTTP status=204(NO CONTENT)を返す
        return '', 204
    else:
        # 存在しないユーザIDが指定された場合
        abort(404)



  #if __name__ == "__main__":
  #    app.run(debug=True)
if __name__ == "__main__":
  app.run(debug=True)