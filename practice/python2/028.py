#함수 밖의 변수는 함수 안으로 못 들어오고, 함수 안의 변수는 함수 밖으로 못 나간다.
#다만, global을 사용하면 함수 밖의 변수를 쓸 수 있다.
x = 10
def xplus(y):
  y += 10
  return y
x = xplus(x)
print(x)
'''
def xplus():
  global x
  x += 10
xplus()
print(x)
'''