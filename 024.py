#무한루프 탈출 구문 설정
'''
x = 0
while True:
  print(x)
  x += 1
'''
x = 0
while True:
  txt = input('제곱할 숫자를 입력하세요:')
  if txt == 'exit':break
  try:
    int(txt)
  except:
    print('숫자를 입력해주세요.')
  else:
    print(int(txt) ** 2)
