##https://dev.classmethod.jp/articles/python-certificate-get-public-key/

import OpenSSL


def get_pubkey(file_path):
    """証明書から公開鍵を取得する."""
    # 証明書をopen
    pem_file = open(file_path, 'rb')

    # byteに変換
    buffer = pem_file.read()

    # 証明書を読み込み
    pemCert = OpenSSL.crypto.load_certificate(
        OpenSSL.crypto.FILETYPE_PEM, buffer)

    # 公開鍵を取得
    pubkey = OpenSSL.crypto.dump_publickey(
        OpenSSL.crypto.FILETYPE_PEM, pemCert.get_pubkey())

    print(pubkey)


get_pubkey('/Users/nishimura.yuji/Downloads/VeriSign-Class 3-Public-Primary-Certification-Authority-G5.pem')