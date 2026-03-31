i = 0

while i < 5:
    print(str(i) + "です")
    #print(i + "です")
    i += 1

# while文
spam = 0
while spam < 5:
  print("Hello!")
  print(spam)
  spam += 1

'''

'''
while True:
  print('あなたの名前を入力してください')
  name = input()
  if name == 'あなたの名前':
    break
print('どうも!')


while True:
  print('あなたはだれ?')
  name = input()
  if name == '':
    continue
  print('やあ、{}パスワードはなに?'.format(name))
  password = input()
  if password == '1234':
    break
print('認証した')
