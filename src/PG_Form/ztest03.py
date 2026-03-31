from src.PG_Common.ComCommon import ComCommon

com = ComCommon("aa")  # インスタンス化
#print(com.a)  # インスタンスからクラス変数を呼び出す

#com.Com_File_Path("c:/")

com.Com_File_Archive('new', 'zip', 'test')

str = [0]
str[0] = "D:\_tmp\ktsDB.bakup"
com.Com_File_Select2(str)
print(str)


'''
str = "D:\_tmp\ktsDB.bakup"
com.Com_File_Select(str)
'''

#com.Lang_Str_Edit("1","2")
## Lang_Str_Edit("1", "2")


