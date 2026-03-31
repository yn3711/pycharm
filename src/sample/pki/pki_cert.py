##https://dev.classmethod.jp/articles/create-x-509-v3-cert-python/
'''
デジタル署名とは、その名の通り文書に「署名」すること。（ここでいう文書とは文字列や数字列といったデータのこと）
では署名に必要な要件とは何か。
第一に、署名をすることができるのは署名者（アリスとする）だけだが、署名を見た人は誰でもそれが有効であることが確認できなければいけない。
第二に、署名と文書は密接に結びついており、別の文書に対するアリスの保証を示すためには使えない。つまり色々な署名からアリスの署名の仕方を推測すること（本当の署名でいうところの筆跡など真似に相当するような行為）、はできないということ。
'''
"""Create Cert."""
from OpenSSL import crypto
from os.path import join

CERT_FILE      = 'test.crt'
KEY_FILE       = 'test.key'
LOCAL_TMP_DIR  = 'tmp/'


def create_cert():
    '''
    暗号理論を使えば上の条件が実現できる。
    公開鍵暗号を用いる方法だ。（公開鍵暗号については
    RSA暗号を実装してみる（知識編） - 技術メモ ）
    具体的にはデジタル署名には３つのスキームで成り立つ。

    1)公開鍵と秘密鍵のペアを生成する(generateKey)
    2)秘密鍵を使って文書に対する署名を生成する(sign)
    3)公開鍵・文書をつかって署名が正しいものかどうかを検証する(verify)
    '''
    #1)公開鍵と秘密鍵のペアを生成する(generateKey)
    ###証明書（cert）を作成
    ## create key pair
    key = crypto.PKey()##キーペアの作成する
    key.generate_key(crypto.TYPE_RSA, 2048) ##「openssl genrsa -out test.key 2048」コマンドにちかいことをしています。

    # create self-signed cert
    cert = crypto.X509() ##インスタンスを生成
    cert.get_subject().C = 'JP'
    cert.get_subject().ST = 'test'
    cert.get_subject().L = 'test'
    cert.get_subject().O = 'test'
    cert.get_subject().OU = 'test'
    cert.get_subject().CN = 'test'
    cert.set_serial_number(1000)
    cert.gmtime_adj_notBefore(0)
    cert.gmtime_adj_notAfter(10 * 365 * 24 * 60 * 60) ##有効期限を設定する。今回の場合10年
    cert.set_issuer(cert.get_subject())
    cert.set_pubkey(key)

    ##v3の拡張属性の設定を行う。
    cert.add_extensions([
        crypto.X509Extension(
            'basicConstraints'.encode('ascii'), False, 'CA:FALSE'.encode('ascii')),
        crypto.X509Extension(
            'keyUsage'.encode('ascii'), True, 'Digital Signature, Non Repudiation'.encode('ascii')),
        crypto.X509Extension(
            'issuerAltName'.encode('ascii'), False, 'email:'.encode('ascii') + 'test'.encode('ascii'))
    ])
    ##v3で生成するように設定する。
    # v3
    cert.set_version(2)

    #2)秘密鍵を使って文書に対する署名を生成する(sign)
    ##自己署名する。
    # self signature
    cert.sign(key, 'sha256')

    ##証明書の情報を取り出す関数。
    ##証明書情報をファイルに書き込んで保存
    # save cert
    open(join(LOCAL_TMP_DIR, CERT_FILE), 'wt').write(
        crypto.dump_certificate(crypto.FILETYPE_PEM, cert).decode('utf-8'))

    ##秘密鍵の情報を取り出す関数・
    ##秘密鍵の情報をファイルに書き込んで保存
    # save private key
    open(join(LOCAL_TMP_DIR, KEY_FILE), 'wt').write(
        crypto.dump_privatekey(crypto.FILETYPE_PEM, key).decode('utf-8'))
    print('ok')


create_cert()
