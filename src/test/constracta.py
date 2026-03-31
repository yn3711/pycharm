# クラスの定義
class Animal:
    # コンストラクタの定義
    def __init__(self, name):
        self.name = name

    # オブジェクトのメソッドを定義
    def say(self):
        print("こんにちは！　私は" + self.name + "です。")

# 2つのオブジェクトを作成する。selfは指定しない。nameに該当する値を指定する
dog = Animal("いぬ")
cat = Animal("ねこ")

# それぞれのオブジェクトのsayメソッドを実行
# 別々の結果が出力される
dog.say()
cat.say()