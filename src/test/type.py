'''5-2 タイプとオブジェクト
　Pythonのtypeとobjectは「鶏が先か、卵が先か」のような関係性を持っています。つまり、どれが先かははっきり説明できないです。そして、typeとobjectは共生関係で、常に同時に出てきます。

　まず、Pythonは「全てがオブジェクト」のプログラミング言語です。そして、3. オブジェクト指向に関する概念で紹介したように、オブジェクト指向の枠組みには主に以下の2種類の関係性が存在します。

継承関係。子クラスは親クラスを継承し、is-aの関係性を作ります。例えば、reptileを継承したsnakeクラスがあるとして、「snake is a kind of reptile」と言えます。親クラスを参照したい時は、__base__が使用できます。
クラス・インスタンス関係。あるタイプのクラスをインスタンス化するとこの関係が生まれます。例えば、Squasherというsnakeのインスタンスを作ることができ、「Squasher is an instance of snake」と言えます。ここのsnakeはSquasherのタイプクラスと定義します。インスタンスのタイプクラスを参照したい時は、__class__か、type()関数が使用できます。
'''

print(object)
# 実行結果：<class 'object'>
print(type)
# 実行結果：<class 'type'>

'''
Pythonの世界では、objectは継承関係の頂点であり、全てのクラスの親クラスになります。
それに対して、typeはクラス・インスタンス関係の頂点で、全てのオブジェクトのタイプクラスになります。
2者の関係性を「object is an instance of type」と表現できます。
'''

print(object.__class__)
# 実行結果：<class 'type'>
print(object.__bases__)  # 継承関係の頂点なので、それ以上は存在しない
# 実行結果：()
print(type.__class__)  # type自身もtypeのインスタンス
# 実行結果：<class 'type'>
print(type.__bases__)
# 実行結果：(<class 'object'>,)

'''
続いて、list、dict、tupleなどのビルトインデータクラスについて見てみます。
'''

print(list.__bases__)
# 実行結果：(<class 'object'>,)
print(list.__class__)
# 実行結果：<class 'type'>
print(dict.__bases__)
# 実行結果：(<class 'object'>,)
print(dict.__class__)
# 実行結果：<class 'type'>
print(tuple.__bases__)
# 実行結果：(<class 'object'>,)
print(tuple.__class__)
# 実行結果：<class 'type'>

'''
親クラスはobjectで、typeのインスタンスになります。
listをインスタンス化して検証してみましょう。
ここのCクラスのインスタンスにも親クラスが存在しません。
'''

mylist = [1, 2, 3]
print(mylist.__class__)
# 実行結果：<class 'list'>
print(mylist.__bases__)
# 実行結果：
# ---------------------------------------------------------------------------
# AttributeError                            Traceback (most recent call last)
# <ipython-input-21-0b850541e51b> in <module>
# ----> 1 print(mylist.__bases__)
#
# AttributeError: 'list' object has no attribute '__bases__'

'''
全てのobjectはtypeのインスタンスです。
typeの直属のインスタンスはobjectやobjectを継承したクラスで、これらはPythonのオブジェクト指向においての「クラス」です。
typeの直属のインスタンス、つまり「クラス」の更なるインスタンスは__bases__を持たないクラスで、これらはPythonのオブジェクト指向においての「インスタンス」です。
　では、typeを継承したクラスはどんなものになるでしょうか？

実はこのMはメタクラスというクラスのクラスです。メタクラスMから作成したTMは上記の図の2列目の「クラス」に所属するでしょう。メタクラスの使い方に関しては後でまた紹介します。

typeは全てのメタクラスの親で、typeを継承してメタクラスを作成できます。
objectは全ての「クラス」の親で、ほとんどのビルトインデータクラスはこの「クラス」です。
「クラス」をインスタンス化して作られたのは「インスタンス」で、継承やインスタンス化に使用できません。
　なぜPythonにはtypeとobject両方必要だろうと思うかもしれません。
例えば、typeがないと、上の図は2列になり、1列目が「タイプクラス」、2列目が「インスタンス」になります。静的オブジェクト指向プログラミング言語は大体この2列の構造です。
Pythonが3列構造になったのは、ランタイムでクラスを動的に作成するためです。
2列目のobjectはただtypeのインスタンスなので、ランタイムでメソッドや属性を変更できるわけです。この性質を実現するために、3列構造が必要になります。
'''
class M(type):
    pass


print(M.__class__)
# 実行結果：<class 'type'>
print(M.__bases__)
# 実行結果：(<class 'type'>,)
