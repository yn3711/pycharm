##****************************************************************************************
##   TITLE   :  担当者マスタ保守   /
##   PROJECT :
##   REMRAKS :https://www.it-swarm-ja.tech/ja/javascript/%E3%83%95%E3%83%A9%E3%82%B9%E3%82%B3%EF%BC%9A%E3%83%9C%E3%82%BF%E3%83%B3%E3%82%92%E3%82%AF%E3%83%AA%E3%83%83%E3%82%AF%E3%81%97%E3%81%A6csv%E3%83%95%E3%82%A1%E3%82%A4%E3%83%AB%E3%82%92%E3%83%80%E3%82%A6%E3%83%B3%E3%83%AD%E3%83%BC%E3%83%89%E3%81%99%E3%82%8B/1053746680/
##****************************************************************************************
from src.PG_Business.CtlEnployee import CtlEmployee
from flask import *

##////////////////////////////////////////////////
##  Class       : FomEmployee
##  Base        :
##  Note        :
##////////////////////////////////////////////////
class FomEmployee:

  # Flaskオブジェクトの生成
  app = Flask(__name__)
  # data = []

  # ルート( / )へアクセスがあった時 --- (*1)
  @app.route("/")
  def root():
    # HTMLでWebフォームを記述 --- (*2)
    return """
    <html><body>
    <form action="/calc" method="post">
      <input type="text" name="a"> ×
      <input type="text" name="b">
      <input type="submit" value="計算">
    </form>
    """

  # フォームの値を受け取って結果を表示 --- (*3)
  @app.route("/calc", methods=["post"])
  def calc():
    ctl = CtlEmployee()  # インスタンス化
    data = ctl.Ctl_Get()
    #ctl.Ctl_Get(data)
    print(data)
    return "<h1>答えは..." + str(data[0].todoufukenname) + "</h1>"
'''
    a = int(request.form.get("a"))
    b = int(request.form.get("b"))
    r = a * b
    return "<h1>答えは..." + str(r) + "</h1>"
'''

# サーバーを起動
if __name__ == "__main__":
    FomEmployee.app.run(debug=True, port=8888)

