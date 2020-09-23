#변경하지 말아야할 데이터는 튜플에 넣는다.
l = [100, 200, 300]
t = (100, 200, 300)
print("함수전", id(l))
def change(i):
  print("함수안", id(i))
  i[0] = 10000
change(t)
print("함수뒤", t)