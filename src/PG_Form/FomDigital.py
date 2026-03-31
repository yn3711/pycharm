##****************************************************************************************
##   TITLE   :
##   PROJECT :
##   REMRAKS :https://swdrsker.hatenablog.com/entry/2018/01/27/080000
##****************************************************************************************
# -*- coding: utf-8 -*-
from src.PG_Common.ComDigital import ComDigital
#from digitalsignature import *
'''
##////////////////////////////////////////////////
##  Class       : FomDigital
##  Base        :
##  Note        :
##////////////////////////////////////////////////
class FomDigital:
    ## -----------------------
    ## クラス変数
    ## クラスが持つ変数で、クラスとインスタンス両方で使えます。
    ## -----------------------
    #com = ""
    #data = []
    #data = [0 for i in range(10)]  # 属性クラスリスト

    ##=====================================================================================
    ## コンストラクタ
    ## @Parameter:
    ## @Return:
    ## @Note:
    ##=====================================================================================
    def __init__(self):
        com = ComDigital()

    ## デストラクタ
    def __del__(self):
        print("del:デストラクタ CtlEmployee")
'''
#co = ComDigital()

# 秘密鍵と公開鍵を作る。（パスワードはなくても良い）
password = "password"
sk, pk = ComDigital.generate_key(passphrase=password)

# メッセージに署名する（署名者が行う）
message = "hoge"
sig = ComDigital.sign(sk, message, passphrase=password)

# 　承認テスト（承認者が行う）
if ComDigital.verify(pk, sig, message):
        print("承認 OK")
else:
        print("承認 NG")

# 　メッセージの書き換えに対するテスト
changed_message = "hogehoge"
if ComDigital.verify(pk, sig, changed_message):
        print("書き換えテスト NG")
else:
        print("書き換えテスト OK")  # 承認されなければOK

# 間違った秘密鍵の署名に対するテスト
sk2, pk2 = ComDigital.generate_key(passphrase=password)
sig2 = ComDigital.sign(sk2, message, passphrase=password)
if ComDigital.verify(pk, sig2, message):
        print("不正署名テスト NG")
else:
        print("不正署名テスト OK")  # 承認されなければOK
