'''

'''
# クラス作成
class Rate:

    rate = 0.1  # クラス変数

    def tax(self, total):
        return int(total * self.rate)

    def tax_amount(self, total):
        return int(total * (1 + self.rate))


# インスタンス化
my_rate = Rate()
print('税額は',my_rate.tax(100))
print('税込金額は',my_rate.tax_amount(100))

Rate.rate = 0.08
print(Rate.rate)



'''

'''
class Person:
    name = '名無し'
    age = 0
    born = '不明'

    def talk(self):
        print('私の名前は{}です。生まれたのは{}で、年齢は{}です。'.format(self.name, self.born, self.age))

ieyasu = Person()
ieyasu.name = 'Ieyasu'
ieyasu.age = 30
ieyasu.born = 'Okazaki'
ieyasu.talk()
print('class変数の値：', Person.age)

'''インスタンス化が行われた際に変数の値を指定しなかった場合、クラス変数を宣言していたらクラス変数の値が使われます。
'''
mituhide = Person()
mituhide.talk()



'''
コンストラクタはインスタンスを生成すると自動で実行するメソッドです。
コンストラクタは __init__ という名前をつけて引数には必ずself を第1引数に指定します。
インスタンス生成時にインスタンス変数を効率よくまとめて作成したい場合にコンストラクタは役にたちます。
尚、インスタンス変数を使いたい場合には、コンストラクタ内で変数宣言する方法が一番スマートで混乱がない方法です。
'''
class Person:
    def __init__(self, n, a, b):
        self.name = n
        self.age = a
        self.born = b

    def talk(self):
        print('私の名前は', self.name, 'です。年齢は', self.age, 'で', self.born, '生まれです。')


tokugawa = Person('家康','18','岡崎')
tokugawa.talk()