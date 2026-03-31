##https://qiita.com/masakielastic/items/05cd6a36bb6fb10fccf6#%E8%87%AA%E5%B7%B1%E7%BD%B2%E5%90%8D%E8%A8%BC%E6%98%8E%E6%9B%B8%E3%81%A8%E7%A7%98%E5%AF%86%E9%8D%B5%E3%81%AE%E7%94%9F%E6%88%90
#自己署名証明書および秘密鍵を生成

from http.server import HTTPServer, SimpleHTTPRequestHandler
import ssl

def run(host, port, ctx, handler):
    server = HTTPServer((host, port), handler)
    server.socket = ctx.wrap_socket(server.socket)
    print('Server Starts - %s:%s' % (host, port))

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    server.server_close()
    print('Server Stops - %s:%s' % (host, port))

if __name__ == '__main__':
    host = 'localhost'
    port = 8000

    #生成
    ctx = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH) #Purpose.SERVER_AUTH (クライアントサイドのソケットを作るのに使う)  Purpose.CLIENT_AUTH (サーバサイドのソケットを作るのに使う)
    ctx.load_cert_chain('./key/server.crt', keyfile='./key/server.key')
    ctx.options |= ssl.OP_NO_TLSv1 | ssl.OP_NO_TLSv1_1
    handler = SimpleHTTPRequestHandler

    run(host, port, ctx, handler)