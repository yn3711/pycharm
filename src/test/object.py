#--
class Human:
    age = 0  # 年齢
    last_name = ''  # 姓
    first_name = ''  # 名前
    blood_type = ''  # 血液型

#--
h = Human()
h.age = 33
h.last_name = '田中'
h.first_name = '一郎'
h.blood_type = 'O'

'''
ythonは__（アンダースコア2つ）から始まる変数や関数は、そのクラス内でしか参照できなくなります。
初期化する時は他のクラスからの影響を受けては困りますので、そのような配慮がなされています。
__init__メソッドを定義してみましょう。
Pythonではオブジェクトが利用する関数を定義する場合、第1引数はオブジェクト自身が自動的に代入される仕組みになっています。
Pythonのselfは、予約語ではありません。self以外の単語も使えますが、慣習としてselfが使われます。 
selfという変数名の代わりに、元のオブジェクトの変数名を使う必要はありません。selfにした方が、誰にとってもわかりやすいでしょう。

'''
class Human:
    def __init__(self, age, last_name, first_name, blood_type):
        self.age = age  # 年齢
        self.last_name = last_name  # 姓
        self.first_name = first_name  # 名前
        self.blood_type = blood_type  # 血液型
#--クラス変数とは、クラス自体が保持する変数のことです。Pythonでは、原則としてクラス名の下に宣言された変数はクラス変数とみなされます。

class Sample1:
    name = 'name' # クラス変数（クラス自体が保持する変数）

print(Sample1.name)  # name
Sample1.name = 'changed_name'
print(Sample1.name)  # changed_name


#--オブジェクト固有の変数のことです。selfキーワードで利用できます。クラス変数のことをクラス属性とも、インスタンス変数のことをデータ属性ともいいます。

class Sample2:
    def __init__(self, value):
        self.value = value

s1 = Sample2('AAA')
s2 = Sample2('BBB')
print(s1.value)  # AAA
print(s2.value)  # BBB
s1.value = 'CCC'
print(s1.value)  # CCC
print(s2.value)  # BBB