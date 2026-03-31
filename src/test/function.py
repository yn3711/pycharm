'''
◯ メソッドを変更する方法
関数をクラスオブジェクトの属性に代入するだけで、 メソッドとして利用できます。
関数は、関数として利用したり、 あるいは複数の異なるクラスのメソッドとして共有して利用したりすることができます。
メソッドを変更したい時は、
クラスオブジェクトの属性に関数を代入します。
'''

#-----------------------
# 対話モード >>> に
# コピペで実行できます。
#-----------------------
class GirlFriend:

    #メンバ関数
    def change_name1(self):
        self.name01 = 'bbbb'

obj_girl_friend = GirlFriend()
obj_girl_friend.change_name1()
print(obj_girl_friend)  # bbbb

#-----------------------
# Step 1:
#     change_name 関数を定義しました。
#-----------------------
def change_name2(self, p_name):
    self.name02 = p_name


#-----------------------
# Step 2:
#     正 クラスオブジェクトの属性に代入する
#        GirlFriend.change_name = change_name
#     誤 インスタンスオブジェクトの属性ではない。
#        girl_friend1.change_name = change_name
#-----------------------
GirlFriend.change_name1 = change_name2

#-----------------------
# Step 3:
#     インスタンスオブジェクトのメソッドは変更される。
#-----------------------
obj_girl_friend.change_name1('aaaa')
print(obj_girl_friend.name02)  # aaaa
print(obj_girl_friend.name01)  # bbbb
