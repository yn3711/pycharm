##****************************************************************************************
##   TITLE   :  担当者マスタ保守  / コントローラ
##   PROJECT :
##   REMRAKS :
##****************************************************************************************
from src.PG_Business.CtlBase import CtlBase  #from モジュール名 import スーパークラス名
from  src.PG_Database.MdlEnployee import MdlEmployee

##////////////////////////////////////////////////
##  Class       : CtlEmployee
##  Base        : tlBase
##  Note        :
##////////////////////////////////////////////////
class CtlEmployee(CtlBase):
    ## -----------------------
    ## クラス変数
    ## クラスが持つ変数で、クラスとインスタンス両方で使えます。
    ## -----------------------
    #mdl = ""
    #data = []
    #data = [0 for i in range(10)]  # 属性クラスリスト

    ##=====================================================================================
    ## コンストラクタ
    ## @Parameter:
    ## @Return:
    ## @Note:
    ##=====================================================================================
    def __init__(self):
        ##DBオープン
        #CtlEmployee.soCon = CtlBase.Bas_DBOpen(self)
        self.con = super().Bas_DBOpen()
        self.mdl = MdlEmployee()

    ## デストラクタ
    def __del__(self):
        print("del:デストラクタ CtlEmployee")
        self.con.close()
    ##======================================================================================
    ## 配列から画面項目へ移送
    ## @Parameter: results
    ## @Return: data
    ## @Note:
    ##======================================================================================
    #@classmethod  # クラスメソッド
    def Ctl_ArrayToFome(self):
        for i in range(len(self.data)):
            for j in range(3):
                if j == 0:
                     print(self.data[i].nendo)
                     nendo=self.data[i].nendo
                elif j == 1:
                       print(self.data[i].dantaicd)
                elif j == 2:
                       print(self.data[i].todoufukenname)
                       break
    ##======================================================================================
    ## テーブル 参照
    ## @Parameter:
    ## @Return:
    ## @Note: selfでアクセスする場合、クラス変数が不変(読み込みのみ)の場合は特に問題ない。
    ##         (注:PythonはJavaでいうfinalに相当する機能がないため、あくまで書き変えをしないで扱いましょうという紳士協定)
    ##======================================================================================
    #@classmethod   # クラスメソッド
    def Ctl_Get(self):
        self.data = self.mdl.Mdl_Get(self.con)
        self.Ctl_ArrayToFome()
        #print(data) error
        print(self.data)
        return self.data
    ##======================================================================================
    ## テーブル 参照
    ## @Parameter:
    ## @Return:
    ## @Note: selfでアクセスする場合、クラス変数が不変(読み込みのみ)の場合は特に問題ない。
    ##         (注:PythonはJavaでいうfinalに相当する機能がないため、あくまで書き変えをしないで扱いましょうという紳士協定)
    ##======================================================================================
    #@classmethod   # クラスメソッド
    def Ctl_Get01(slf):
        cur= slf.con.cursor()
        cur.execute('SELECT * FROM m_system;')
        results = cur.fetchall()
        print(results) ## output result


