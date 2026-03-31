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
    #data = [0 for i in range(len(results))]
    #pty01 = [0 for i in range(10)]
    #pty01 = [PtyEmployee for i in range(10)]

    ##=====================================================================================
    ## コンストラクタ
    ## @Parameter:
    ## @Return:
    ## @Note:
    ##=====================================================================================
    def __init__(self, name="yn"):
        #self.pty = PtyEmployee
        self.name = name
    #def __del__(self):
    #    # デストラクタ
    #    print("del:デストラクタ")

    ##======================================================================================
    ## テーブル項目を変数へ移送
    ## @Parameter:
    ## @Return:
    ## @Note:
    ##======================================================================================
    #@classmethod  # クラスメソッド
    def Mdl_ToArray(self,results):
        #print(results[0][2])
        #dcnt = 0
        #data = [[0 for i in range(10)] for j in range(10)]

        pty01 = [0 for i in range(len(results))]
        #pty01 = [PtyEmployee for i in range(10)]

        data=[0 for i in range(len(results))]
        #pty = copy.deepcopy(PtyEmployee)

        pty = PtyEmployee()  #PtyEmployeeだと同じアドレス

        for i,gyo in enumerate(results):
            #dcnt = dcnt + 1 #カウンタ
            #print(dcnt)
            #print(i)
            #print(gyo[3])
            #print(gyo)
            #print(self.pty)
            #MdlEmployee.pty01[i] = PtyEmployee

            #MdlEmployee.pty01[i] = copy.deepcopy(pty)


            pty01[i] = pty.copy()

            print(pty01)

            #print(MdlEmployee.pty01)
            for j,retsu in enumerate(gyo):
                #print(j)
                if j == 0:
                   #print(retsu)
                   pty01[i].nendo = retsu
                elif j == 1:
                    #print(retsu)
                    pty01[i].dantaicd = retsu
                elif j == 2:
                    pty01[i].todoufukenname = retsu
                    #data[i] = self.pty
                    break

                #data[i][j] = retsu
            data[i] = pty01[i]
            print(pty01[i])
            print(data[i])
            #print(self.pty.nendo)
            #print(self.pty.dantaicd)
            #print(self.pty.todoufukenname)
            print(i)
            print(data[i].nendo)
            print(data[0].nendo)
        print(data[2].nendo)
        #print(self.pty.nendo)
        #print(self.pty.dantaicd)
        #print(self.pty.todoufukenname)
        #print(data)

            #print(row[1])
            #print(row[2])
            #print(row[3])
            #n += 1


            #pty.nendo = row[i]
            #pty.dantaicd = row[1]
            #pty.todoufukenname = row[2]
            #tbl[0] = pty
            #print(tbl.nendo)



        ##ひとつずつ取得する
        #for row in cur:
        #    print(row)


        ## output result

    ##======================================================================================
    ## テーブル参照
    ## @Parameter:
    ## @Return:
    ## @Note: #MdlEmployee("yn")
    ##======================================================================================
    ## @classmethod   # クラスメソッド
    def Mdl_Get(self, con):

        tbl = []

        #pty = PtyEmployee
        ## カーソルを開く
        cur = con.cursor()
        cur.execute('SELECT * FROM m_system;')

        ##まとめて取得する
        results = cur.fetchall()

        self.Mdl_ToArray(results)


        ##実行結果のカラム名を取得する
        #colnames = [col.name for col in cur.description]
        #print(colnames)

        #with get_connection() as soCon:
        #with soCon.cursor(cursor_factory=DictCursor) as cur:
        #        cur.execute('SELECT * FROM m_system;')
        #        row = cur.fetchone()
        #        print(row)  # => { "count": 123 }


        cur.close()

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
        cur = soCon.cursor()
        cur.execute('SELECT * FROM m_system;')

        ##まとめて取得する
        results = cur.fetchall()
        # print(results)

        df1 = pd.DataFrame(results)
        print(df1)


        cur.close()



