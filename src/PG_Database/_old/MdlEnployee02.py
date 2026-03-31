##****************************************************************************************
##   TITLE   :  担当者マスタ／モデル
##   SYSTEM  :
##
##   PROJECT :
##   FILE-ID :
##
##   WRITE   :  99/99/99
##   UPDATE  :
##
##   REMRAKS :
##
##****************************************************************************************
from src.PG_Database.MdlBase import *   #from モジュール名 import スーパークラス名
from src.PG_Database.PtyEnployee import *

from psycopg2.extras import DictCursor
import pandas as pd

##////////////////////////////////////////////////
##  Class       : MdlEmployee
##  Base        : MdlBase
##  Note        :
##////////////////////////////////////////////////
class MdlEmployee(MdlBase):

    ## -----------------------
    ## クラス変数
    ## クラスが持つ変数で、クラスとインスタンス両方で使えます。
    ## -----------------------
    cur = ""

    ##=====================================================================================
    ## コンストラクタ
    ## @Parameter:
    ## @Return:
    ## @Note:
    ##=====================================================================================
    def __init__(self, name=""):
        #self.pty = PtyEmployee
        self.name = name

    ## デストラクタ
    def __del__(self):
        print("del:デストラクタ PtyEmployee")
        self.cur.close()
    ##======================================================================================
    ## テーブル項目を変数へ移送
    ## @Parameter: results
    ## @Return: data
    ## @Note:
    ##======================================================================================
    #@classmethod  # クラスメソッド
    def Mdl_DbToSet(self,results):
        data = [0 for i in range(len(results))]  #属性クラスリスト
        pty01 = [0 for i in range(len(results))] #work
        pty = PtyEmployee()  # 注)PtyEmployeeだと同じアドレスを参照

        for i,gyo in enumerate(results):
            pty01[i] = pty.copy()
            for j,retsu in enumerate(gyo):
                if j == 0:
                   pty01[i].nendo = retsu
                elif j == 1:
                    pty01[i].dantaicd = retsu
                elif j == 2:
                    pty01[i].todoufukenname = retsu
                    break
            data[i] = pty01[i]

        return data
    ##======================================================================================
    ## テーブル参照
    ## @Parameter:
    ## @Return:
    ## @Note: #MdlEmployee("yn")
    ##======================================================================================
    ## @classmethod   # クラスメソッド
    def Mdl_Get(self, con):
        data = []

        ## カーソルを開く
        self.cur = con.cursor()
        self.cur.execute('SELECT * FROM m_system;')

        ##まとめて取得する
        results = self.cur.fetchall()

        ##テーブル項目をセット
        data = self.Mdl_DbToSet(results)

        #print(data)

        ##実行結果のカラム名を取得する
        #colnames = [col.name for col in cur.description]
        #print(colnames)
        return data
    ##======================================================================================
    ## テーブル参照
    ## @Parameter:
    ## @Return:
    ## @Note: https://qiita.com/yuta-38/items/cde48b5ba56736e4e179
    ##======================================================================================
    ## @classmethod   # クラスメソッド
    def Mdl_Get01(self, soCon):
        tbl = []

        #pty = PtyEmployee
        ## カーソルを開く
        self.cur = soCon.cursor()
        self.cur.execute('SELECT * FROM m_system;')

        ##まとめて取得する
        results = self.cur.fetchall()
        # print(results)

        df1 = pd.DataFrame(results)
        print(df1)
