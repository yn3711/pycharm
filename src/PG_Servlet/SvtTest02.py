##****************************************************************************************
##   TITLE   :
##   PROJECT :
##   REMRAKS : https://naporitan.hatenablog.com/entry/2019/02/06/011740
##****************************************************************************************
from flask import Flask, jsonify, render_template
from flask_cors import CORS
from flask_restful import Api, Resource, reqparse

app = Flask(__name__, static_folder="dist/static", template_folder="dist")
CORS(app)
api = Api(app)

##////////////////////////////////////////////////
##  Class       :
##  Base        :
##  Note        : get, post, put, deleteリクエストがあったときの処理をそれぞれ書く
##////////////////////////////////////////////////
class SvtTest02(Resource):

        parser = reqparse.RequestParser()
        # add_argumentでパラメータを取得できます
        # この辺はflask_restfulの公式ドキュメントに色々乗ってるのでそっち見た方がよさげ
        parser.add_argument("message")

        def get(self):
            args = self.parser.parse_args()
            return {"message": args["message"]}

        def post(self):
            args = self.parser.parse_args()
            return {"message": args["message"]}

        def put(self):
            args = self.parser.parse_args()
            return {"message": args["message"]}

        def delete(self):
            args = self.parser.parse_args()
            return {"message": args["message"]}

api.add_resource(SvtTest02, "/api/test")

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def get_vue(path):
    return render_template('index.html')

# 一応エラーハンドラ

@app.errorhandler(403)
@app.errorhandler(404)
@app.errorhandler(500)
def error_handler(error):
    msg = 'Error: {code}'.format(code=error.code)
    return jsonify({"result": "Failed",
                    "message": msg,
                    "errorcode": error.code})

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)