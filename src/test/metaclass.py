
x = 30
print(x.__class__)
# 実行結果：<class 'int'>
print(x.__class__.__class__)
# 実行結果：<class 'type'>

class Meta(type):
    pass


class Foo(metaclass=Meta):
    pass

'''
5-3-4. メタクラスの使い方
　メタクラスを使う目的は、クラスの作成時に、自動的に何らかのカスタマイズをすることです。例えば、あるモジュールにおいて、全てのクラスの属性名を大文字にしたい時に、このようなメタクラスが作れます。
'''

class UpperAttrMetaClass(type):
    # __new__はインスタンスselfを作成するコンストラクタ
    # __init__は作成されたインスタンスselfを初期化するイニシャライザ
    def __new__(cls, new_class_name,
                new_class_parents, new_class_attr):
        uppercase_attr = {}
        for name, val in new_class_attr.items():
            # 特殊メソッドを除く
            if not name.startswith('__'):
                uppercase_attr[name.upper()] = val
            else:
                uppercase_attr[name] = val
        return type.__new__(cls, new_class_name, new_class_parents, new_class_attr)
        # 下の書き方と同様
        # return super().__new__(cls, new_class_name, new_class_parents, new_class_attr)