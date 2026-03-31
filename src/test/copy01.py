import copy


class Sample():

    def __init__(self, text):
        self.text = text

    def __repr__(self):
        return self.text

    def __deepcopy__(self, memo):
        """ 自分自身と同じオブジェクトを生成し、返す """
        new_obj = Sample(self.text)
        return new_obj


# その3 深いコピー
data1 = {'key1': 100, 'key2': Sample('obj')}
data2 = copy.deepcopy(data1)

# コピーされていることを確認する
data2['key2'].text = 'hoge'
print(data1)
print(data2)