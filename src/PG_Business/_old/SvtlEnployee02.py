##****************************************************************************************
##   TITLE   :  担当者マスタ保守  / サーブレット
##   SYSTEM  :
##
##   PROJECT :
##   FILE-ID :  SvtTantousya
##
##   WRITE   :  99/99/99
##   UPDATE  :  99/99/99
##
##   REMRAKS : 複数のポートでリッスン
#              https://www.366service.com/jp/qa/ba19ca45cefd3f7c7d8c05b5488d2f4a
##             https://qiita.com/shiracamus/items/debf1dd4f15facaa0067
##
##****************************************************************************************
from src.PG_Servlet.SvtBase import SvtBase  #from モジュール名 import スーパークラス名
from threading import Thread
from socketserver import ThreadingMixIn
from http.server import HTTPServer, BaseHTTPRequestHandler

##////////////////////////////////////////////////
##  Class       : SvtEmployee
##  Base        :
##  Note        : クエストを処理するハンドラ
##////////////////////////////////////////////////
class SvtEmployee(BaseHTTPRequestHandler,SvtBase):
    ## -----------------------
    ## クラス変数
    ## クラスが持つ変数で、クラスとインスタンス両方で使えます。
    ## -----------------------


    ##=====================================================================================
    ## コンストラクタ
    ## @Parameter:
    ## @Return:
    ## @Note:
    ##=====================================================================================
    #def __init__(self):
    ## デストラクタ
    #def __del__(self):
    ##======================================================================================
    ## do_GET
    ## @Return:
    ## @Note:
    ##======================================================================================
    #@classmethod   # クラスメソッド

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(bytes("Hello World!", "utf-8"))


class ThreadingHTTPServer(ThreadingMixIn, HTTPServer):
    pass

def serve_on_port(port):
    server = ThreadingHTTPServer(("localhost", port), SvtEmployee)
    server.serve_forever()



Thread(target=serve_on_port, args=[1111]).start()
serve_on_port(2222)