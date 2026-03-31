'''
https://xtech.nikkei.com/atcl/learning/lecture/19/00108/00005/

クラス名の指定は関数と同じ様に「class クラス名:」とすればOKです。
※ちなみにクラス名は大文字で記述するのが一般的です。
'''


# class宣言
class Human:

    # コンストラクタ
    '''
    関数の様に定義された「def __init__～」の部分をコンストラクタと言います。
    Javaなどでもコンストラクタがありますが、Pythonの場合は「__init__」で記載します。

    「del オブジェクト名」でデストラクタを実行できます。

    「self」という記述が出てきますが、このselfはインスタンス自身を指す変数です。
    ※他の言語によっては「this」などで扱われる事があります。
    '''
    def __init__(self, name, year, birth):
        self.name = name
        self.year = year
        self.birth = birth
    '''
    Javaなど他のオブジェクト指向言語では、メンバには「プライベート（インスタンス外からアクセスできない）」と
    「パブリック（インスタンス外からもアクセスできる）」の2種類があるものがあります。
    しかしPythonでは、メンバは全てパブリック、つまりインスタンス外からアクセス可能です。
    アクセスを制限したいときは、「プロパティ」という手法を使います
    '''
    # 関数は「def 」というキーワードで定義
    # 自己紹介メソッド
    def introduce(self):
        text = "私の名前は、{}です。今年で{}歳になります。"
        return text.format(self.name, self.year)

    # 加齢メソッド
    def grow_old(self, after):
        self.year += after
'''
「class クラス名（基底クラス名）:」という記述で継承する事ができます。
 '''
# Humanクラスを継承して、HumanHealthを定義
class HumanHealth(Human):
    # コンストラクタ
    def __init__(self, name, year, birth, height, weight):

        #親クラスのコンストラクタを呼び出す
        super().__init__(name, year, birth)

        self.height = height
        self.weight = weight

    # BMIメソッドを追加
    def get_bmi(self):
        return round(self.weight/(self.height**2),2)

        # 自己紹介メソッドをオーバーライド

    def introduce(self):
        text = "私の名前は、{}です。今年で{}歳になります。BMIは{}です。"
        return text.format(self.name, self.year, self.get_bmi())



# インスタンス作成
souma_human = Human("souma", 26, "19931013")

# 自己紹介メソッド呼び出し
souma_introduce = souma_human.introduce()

# 出力
print (souma_introduce)

# 加齢メソッド呼び出し
souma_human.grow_old(2)
print (souma_human.introduce())




souma = HumanHealth("souma", 26, "19931013", 1.7, 70)
# 子メンバ
print (souma.height)
# 子メンバ
print (souma.weight)
# 子メソッド
print (souma.get_bmi())
# 親メソッド
print (souma.introduce())


souma = HumanHealth("souma", 26, "19931013", 1.7, 70)
# オーバーライド
print (souma.introduce())