##****************************************************************************************
##   TITLE   :  担当者マスタ保守  / ビジネス層コントローラ
##   SYSTEM  :
##
##   PROJECT :
##   FILE-ID :  CtlTantousya
##
##   WRITE   :  99/99/99
##   UPDATE  :  99/99/99
##
##   REMRAKS :
##****************************************************************************************
from .CtlBase import CtlBase  #from モジュール名 import スーパークラス名

class CtlEmployee(CtlBase):
    ## -----------------------
    ## クラス変数
    ## クラスが持つ変数で、クラスとインスタンス両方で使えます。
    ## -----------------------
    soCon = ""

    ##=====================================================================================
    ## コンストラクタ
    ## @Parameter: ｲﾝｽﾀﾝｽ変数初期値
    ## @Return: Void
    ## @Note:
    ##=====================================================================================
    def __init__(self, name):
        self.name = name
        ##DBオープン
        #CtlEmployee.soCon = CtlBase.Bas_DBOpen(self)
        CtlEmployee.soCon = super().Bas_DBOpen()

    ##======================================================================================
    ## テーブル参照
    ## @Parameter:
    ## @Return:
    ## @Note:
    ##======================================================================================
    ## @classmethod   # クラスメソッド
    def Ctl_Get(self):
        cur= CtlEmployee.soCon.cursor()
        cur.execute('SELECT * FROM m_system;')
        results = cur.fetchall()

        ## output result
        print(results)

    ##======================================================================================
    ## テーブル参照
    ## @Parameter:
    ## @Return:
    ## @Note:
    ##======================================================================================
    @classmethod   # クラスメソッド
    def Cmd_Get01(cls):
        cur= cls.soCon.cursor()
        cur.execute('SELECT * FROM m_system;')
        results = cur.fetchall()

        ## output result
        print(results)


