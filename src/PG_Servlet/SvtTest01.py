##****************************************************************************************
##   TITLE   :
##   PROJECT :
##   REMRAKS : https://qiita.com/__init__/items/5c89fa5b37b8c5ed32a4
##****************************************************************************************
import socket

##////////////////////////////////////////////////
##  Class       :
##  Base        :
##  Note        :
##////////////////////////////////////////////////
class SvtTest01():

    # AF = IPv4 という意味
    # TCP/IP の場合は、SOCK_STREAM を使う
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # IPアドレスとポートを指定
        s.bind(('127.0.0.1', 50007))
        # 1 接続
        s.listen(1)
        # connection するまで待つ
        while True:
            # 誰かがアクセスしてきたら、コネクションとアドレスを入れる
            conn, addr = s.accept()
            with conn:
                while True:
                    # データを受け取る
                    data = conn.recv(1024)
                    if not data:
                        break
                    print('data : {}, addr: {}'.format(data, addr))
                    # クライアントにデータを返す(b -> byte でないといけない)
                    conn.sendall(b'Received: ' + data)
