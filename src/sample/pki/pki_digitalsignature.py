##https://swdrsker.hatenablog.com/entry/2018/01/27/080000
'''
デジタル署名とは、その名の通り文書に「署名」すること。（ここでいう文書とは文字列や数字列といったデータのこと）
では署名に必要な要件とは何か。
第一に、署名をすることができるのは署名者（アリスとする）だけだが、署名を見た人は誰でもそれが有効であることが確認できなければいけない。
第二に、署名と文書は密接に結びついており、別の文書に対するアリスの保証を示すためには使えない。
      つまり色々な署名からアリスの署名の仕方を推測すること（本当の署名でいうところの筆跡など真似に相当するような行為）、はできないということ。
という２つの要件が必要になってくる。
'''
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256
from base64 import b64decode, b64encode
import sys

'''
暗号理論を使えば上の条件が実現できる。
公開鍵暗号を用いる方法だ。（公開鍵暗号については RSA暗号を実装してみる（知識編） - 技術メモ ）
具体的にはデジタル署名には３つのスキームで成り立つ。
１）公開鍵と秘密鍵のペアを生成する (generateKey)
２）秘密鍵を使って文書に対する署名を生成する (sign)
３）公開鍵・文書をつかって署名が正しいものかどうかを検証する (verify)
署名者（アリスとする）はgenerateKeyを使って秘密鍵skと公開鍵pkを生成し、公開鍵を公開する。
アリスは署名したい文書Dataをハッシュ関数にかけたうえで秘密鍵skを使って署名signatureを生成する。
承認者は公開されている公開鍵pk・文書Data・アリスから受け取った署名signatureを使って、pk,Data,signatureの組が正当であればTrueを返し違っていればFalseを返す。署名が間違っているか文書が書き換えられていれば承認がうまくいかないことになる。
'''

##１）公開鍵と秘密鍵のペアを生成する (generateKey)
def generate_key(keysize=2048, passphrase = None):
    new_key = RSA.generate(keysize)
    public_key = new_key.publickey().exportKey()
    secret_key = new_key.exportKey(passphrase = passphrase)
    return secret_key, public_key

##２）秘密鍵を使って文書に対する署名を生成する (sign)
def sign(secret_key, data, passphrase = None):
    try:
        rsakey = RSA.importKey(secret_key, passphrase = passphrase)
    except ValueError as e:
        print(e)
        sys.exit(1)
    signer = PKCS1_v1_5.new(rsakey)
    digest = SHA256.new()
    digest.update(b64decode(data))
    sign = signer.sign(digest)
    return b64encode(sign)

##３）公開鍵・文書をつかって署名が正しいものかどうかを検証する (verify)
def verify(pub_key, signature, data):
    rsakey = RSA.importKey(pub_key)
    signer = PKCS1_v1_5.new(rsakey)
    digest = SHA256.new()
    digest.update(b64decode(data))
    if signer.verify(digest, b64decode(signature)):
        return True
    else:
        return False