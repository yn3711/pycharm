##****************************************************************************************
##   TITLE   :  担当者マスタ／モデル
##   PROJECT :
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
    results=""
    cur = ""
    data=[]
    ##=====================================================================================
    ## コンストラクタ
    ## @Parameter:
    ## @Return:
    ## @Note:
    ##=====================================================================================
    def __init__(self, name=""):
        self.pty = PtyEmployee()
        self.name = name

    ## デストラクタ
    def __del__(self):
        print("del:デストラクタ PtyEmployee")
        self.cur.close()
    ##======================================================================================
    ## テーブル項目を配列へ移送
    ## @Parameter: results
    ## @Return: data
    ## @Note:
    ##======================================================================================
    #@classmethod  # クラスメソッド
    def Mdl_DbToArray(self):
        self.data = [0 for i in range(len(self.results))]  # 属性クラスリスト
        record= [0 for i in range(len(self.results))] #work
        #pty = PtyEmployee()  # 注)PtyEmployeeだと同じアドレスを参照

        for i,gyo in enumerate(self.results):
            record[i] = self.pty.copy() #record

            for j,retsu in enumerate(gyo):
                if j == 0:
                   record[i].nendo = retsu
                elif j == 1:
                    record[i].dantaicd = retsu
                elif j == 2:
                    record[i].todoufukenname = retsu
                    break
            self.data[i] = record[i]
            #print(data)

        #return data
    ##======================================================================================
    ## テーブル参照
    ## @Parameter:
    ## @Return:
    ## @Note: #MdlEmployee("yn")
    ##======================================================================================
    ## @classmethod   # クラスメソッド
    def Mdl_Get(self, con):
        #data = []

        ## カーソルを開く
        self.cur = con.cursor()
        self.cur.execute('SELECT * FROM uid_kts.m_system;')

        ##まとめて取得する
        self.results = self.cur.fetchall()

        ##テーブル項目をセット
        #data = self.Mdl_DbToSet(results)
        self.Mdl_DbToArray()

        print(self.data)

        ##実行結果のカラム名を取得する
        #colnames = [col.name for col in cur.description]
        #print(colnames)

        return self.data
    ##======================================================================================
    ## テーブル参照
    ## @Parameter:
    ## @Return:
    ## @Note: https://qiita.com/yuta-38/items/cde48b5ba56736e4e179
    ##======================================================================================
    ## @classmethod   # クラスメソッド
    def Mdl_Get01(self, soCon):
        #tbl = []

        #pty = PtyEmployee
        ## カーソルを開く
        self.cur = soCon.cursor()
        self.cur.execute('SELECT * FROM m_system;')

        ##まとめて取得する
        results = self.cur.fetchall()
        # print(results)

        df1 = pd.DataFrame(self.results)
        print(df1)
