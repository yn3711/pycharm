##****************************************************************************************
##   TITLE   :
##   PROJECT :
##   REMRAKS : 複数のポートでリッスン
#              https://www.366service.com/jp/qa/ba19ca45cefd3f7c7d8c05b5488d2f4a
##             https://qiita.com/shiracamus/items/debf1dd4f15facaa0067
##
##****************************************************************************************
from src.PG_Servlet.SvtBase import SvtBase  #from モジュール名 import スーパークラス名
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
        self.end_headers()
        #message = threading.currentThread().getName()
        #self.wfile.write(message)
        self.wfile.write(bytes("Hello World!", "utf-8"))
        return

class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    """Handle requests in a separate thread."""

if __name__ == '__main__':
    server = ThreadedHTTPServer(('localhost', 8080), SvtEmployee)
    print
    'Starting server, use <Ctrl-C> to stop'
    print ('http://localhost:8080')
    server.serve_forever()