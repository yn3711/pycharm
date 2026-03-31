##****************************************************************************************
##   TITLE   :  担当者マスタ／プロパティ
##   PROJECT :
##   REMRAKS :
##
##****************************************************************************************
import copy

##////////////////////////////////////////////////
##  Class       : PtyEmployee
##  Base        :
##  Note        :
##////////////////////////////////////////////////
class PtyEmployee:

    ## -----------------------
    ## クラス変数
    ## クラスが持つ変数で、クラスとインスタンス両方で使えます。
    ## -----------------------

    ##=====================================================================================
    ## コンストラクタ
    ## @Parameter:
    ## @Return:
    ## @Note:
    ##=====================================================================================
    def __init__(self, nendo="", dantaicd="", todoufukenname=""):
        self.__nendo = nendo
        self.__dantaicd = dantaicd
        self.__todoufukenname = todoufukenname

    #def __deepcopy__(self):
    #    """ 自分自身と同じオブジェクトを生成し、返す """
    #    new_obj = PtyEmployee(self)
    #    return new_obj
    def copy(self):
        return copy.deepcopy(self)
    ##======================================================================================
    ## テーブル項目を変数へ移送
    ## @Parameter:
    ## @Return:
    ## @Note:
    ##======================================================================================
    #def Pty_ToArry(self):


    ##======================================================================================
    ## 項目参照
    ## @Parameter:
    ## @Return:
    ## @Note:
    ##======================================================================================
    @property  # @propertyとすると、getterとして定義できる
    def nendo(self):
        #print("getterを呼び出しました")
        return self.__nendo

    @property
    def dantaicd(self):
        return self.__dantaicd

    @property
    def todoufukenname(self):
        return self.__todoufukenname



    ##======================================================================================
    ## 項目Set
    ## @Parameter:
    ## @Return:
    ## @Note:
    ##======================================================================================
    @nendo.setter  # setterとして定義する。
    def nendo(self, value):
        #print("setterを呼び出しました")
        self.__nendo = value

    @dantaicd.setter
    def dantaicd(self, value):
        self.__dantaicd = value

    @todoufukenname.setter
    def todoufukenname(self, value):
        self.__todoufukenname = value



    ##======================================================================================
    ## 項目削除
    ## @Parameter:
    ## @Return:
    ## @Note:
    ##======================================================================================
    @nendo.deleter  # deleterとして定義される。
    def nendo(self):
        #print("deleterを呼び出しました")
        del self.__nendo

    @dantaicd.deleter
    def dantaicd(self):
        del self.__dantaicd

    @todoufukenname.deleter
    def todoufukenname(self):
        del self.__todoufukenname
