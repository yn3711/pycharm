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
from src.PG_Business.CtlBase import CtlBase  #from モジュール名 import スーパークラス名
from  src.PG_Database.MdlEnployee import MdlEmployee


class CtlEmployee(CtlBase):
    ## -----------------------
    ## クラス変数
    ## クラスが持つ変数で、クラスとインスタンス両方で使えます。
    ## -----------------------
    soCon = ""

    ##=====================================================================================
    ## コンストラクタ
    ## @Parameter:
    ## @Return:
    ## @Note:
    ##=====================================================================================
    def __init__(self):
        ##DBオープン
        #CtlEmployee.soCon = CtlBase.Bas_DBOpen(self)
        CtlEmployee.soCon = super().Bas_DBOpen()
        #self.soCon = super().Bas_DBOpen()
    ##======================================================================================
    ## テーブル参照
    ## @Parameter:
    ## @Return:
    ## @Note:
    ##======================================================================================
    @classmethod   # クラスメソッド
    def Ctl_Get(cls):
        mdl = MdlEmployee()
        mdl.Mdl_Get(cls.soCon)
        cls.soCon.close()

    ##======================================================================================
    ## テーブル参照
    ## @Parameter:
    ## @Return:
    ## @Note: selfでアクセスする場合、クラス変数が不変(読み込みのみ)の場合は特に問題ない。
    #         (注:PythonはJavaでいうfinalに相当する機能がないため、あくまで書き変えをしないで扱いましょうという紳士協定)
    #
    ##======================================================================================
    #@classmethod   # クラスメソッド
    def Ctl_Get01(slf):
        cur= slf.soCon.cursor()
        cur.execute('SELECT * FROM m_system;')
        results = cur.fetchall()

        ## output result
        print(results)


