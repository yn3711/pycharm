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
##   REMRAKS :
##****************************************************************************************
import argparse
import cgi
import io
#import socketserver import ThreadingTCPServer, BaseRequestHandler
import sys
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs, urlparse

address = ('localhost', 8080)
##////////////////////////////////////////////////
##  Class       : SvtEmployee
##  Base        :
##  Note        : クエストを処理するハンドラ
##////////////////////////////////////////////////
class SvtEmployee(BaseHTTPRequestHandler):
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
    ##
    ## @Return:
    ## @Note:
    ##======================================================================================
    #@classmethod   # クラスメソッド
    def gen_message(self):
        """HTTPメソッドに共通したメッセージを生成する"""
        parsed_path = urllib.parse.urlparse(self.path)
        message_parts = [
            "CLIENT_VALUES:",
            "client_address={} ({})".format(self.client_address, self.address_string()),
            "command={}".format(self.command),
            "path={}".format(self.path),
            "real_path={}".format(parsed_path.path),
            "query={}".format(parsed_path.query),
            "request_version".format(self.request_version),
            "",
            "SERVER VALUES:",
            "server_version={}".format(self.server_version),
            "sys_version={}".format(self.sys_version),
            "protocol_version={}".format(self.protocol_version),
            "",
            "HEADERS RECEIVED:"
        ]
        for name, value in sorted(self.headers.items()):
            message_parts.append("{}={}".format(name, value.rstrip()))
        else:
            message_parts.append("")
        message = "\n".join(message_parts)
        return message

    def do_GET(self):
        print('path = {}'.format(self.path))
        parsed_path = urlparse(self.path)
        print('parsed: path = {}, query = {}'.format(parsed_path.path, parse_qs(parsed_path.query)))
        print('headers\r\n-----\r\n{}-----'.format(self.headers))

        #self.send_response(http.HTTPStatus.OK)
        self.send_response(200)
        #self.send_header('Content-length', len(message))
        self.send_header("User-Agent", "test1")
        self.send_header('Content-Type', 'text/plain; charset=utf-8')
        self.end_headers()
        html = "abc"
        self.wfile.write(html.encode())
        #self.wfile.write(message.encode("utf8"))

    def do_POST(self):
        print('path = {}'.format(self.path))
        parsed_path = urlparse(self.path)
        print('parsed: path = {}, query = {}'.format(parsed_path.path, parse_qs(parsed_path.query)))
        print('headers\r\n-----\r\n{}-----'.format(self.headers))
        content_length = int(self.headers['content-length'])
        print('body = {}'.format(self.rfile.read(content_length).decode('utf-8')))

        #self.send_response(http.HTTPStatus.OK)
        self.send_response(200)
        self.send_header('Content-Type', 'text/plain; charset=utf-8')
        self.end_headers()
        self.wfile.write(b'Hello from do_POST')

        #self.wfile.write(message.encode("utf8"))
        self.wfile.write("\n".encode("utf8"))

        out = io.TextIOWrapper(
            self.wfile,
            encoding="utf8",
            line_buffering=False,
            write_through=True,
        )

        out.write("FORM DATA:\n")

        for field in form.keys():
            field_item = form[field]
            if field_item.filename:
                file_data = field_item.file.read()
                file_len = len(file_data)
                del file_data
                out.write("Upload {} as {!r} ({} bytes)\n".format(field, field_item.filename, file_len))
            else:
                out.write("{}={}\n".format(field, form[field].value))
        else:
            out.detach()

#class ThreadedHTTPServer(socketserver.ThreadingMixIn, http.server.HTTPServer):
#class ThreadedHTTPServer(socketserver.ThreadingMixIn, HTTPServer):
#    """HTTPリクエストをスレッドに分割して処理するHTTPサーバー"""
#    pass

#class ForkedHTTPServer(socketserver.ForkingMixIn, http.server.HTTPServer):
#class ForkedHTTPServer(socketserver.ForkingMixIn, HTTPServer):
#    """HTTPリクエストをプロセスに分割して処理するHTTPサーバー"""
#    pass

def runserver(server, handler, protocol="HTTP/1.0", port=8000, bind=""):
    server_address = (bind, port)
    handler.protocol_version = protocol
    httpd = server(server_address, handler)
    sa = httpd.socket.getsockname()
    serve_message = "Serving HTTP on {host} port {port} (http://{host}:{port}/) ..."
    print(serve_message.format(host=sa[0], port=sa[1]))
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nKeyboard interrupt received, exiting.")
        sys.exit(0)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--thread', action='store_true', help='Run Threading HTTP Server')
    parser.add_argument('--process', action='store_true', help='Run Processing HTTP Server')
    parser.add_argument('--bind', '-b', default='', metavar='ADDRESS',
                        help='Specify alternate bind address '
                             '[default: all interfaces]')
    parser.add_argument('port', action='store',
                        default=8000, type=int,
                        nargs='?',
                        help='Specify alternate port [default: 8000]')
    args = parser.parse_args()


    if args.thread:
        server = ThreadedHTTPServer
    elif args.process:
        server = ForkedHTTPServer
    else:
        #server = http.server.HTTPServer
        server = HTTPServer

    handler = SvtEmployee

    runserver(server=server, handler=handler, port=args.port, bind=args.bind)

#with HTTPServer(address, SvtEmployee) as server:
#     server.serve_forever()