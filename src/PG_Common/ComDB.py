##****************************************************************************************
##   TITLE   : DB
##   PROJECT :　
##   FILE-ID :  ComDB.py
##   REMRAKS :
##****************************************************************************************
import psycopg2

##////////////////////////////////////////////////
##  Class       : CommonDB
##  Base        :
##  Note        :
##////////////////////////////////////////////////
class ComDB:
    ## -----------------------
    ## インスタンス変数
    ## -----------------------


    ##=====================================================================================
    ## コンストラクタ
    ## @Parameter:
    ## @Return:
    ## @Note:
    ##=====================================================================================
    #def __init__(self):

    ##======================================================================================
    ##   ＤＢ接続
    ##   @Parameter :
    ##   @Return    :
    ##   @Note :
    ##======================================================================================
    def  Com_DBconnect(self,ptHOST, ptPORT, ptDBNAME, ptUID, ptPWD):
    #def Com_DBOpen(self):

      conn = psycopg2.connect("host=" + ptHOST +
                               " port=" + ptPORT +
                               " dbname=" + ptDBNAME +
                               " user=" + ptUID +
                               " password=" + ptPWD)
      return conn
'''    def Com_DBconnect(self):
        conn =  psycopg2.connect("host=" + "localhost" +
                                " port=" + "5433" +
                                " dbname=" + "ktsDB" +
                                " user=" + "postgres" +
                                " password=" + "postgres")

        return conn
'''
