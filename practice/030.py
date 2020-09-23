#함수의 클로저 : 함수에 독립적인 환경을 제공함
x = 100
def f():
  x = 10
  def xPlus():
    nonlocal x #가장 가까운 x를 가져온다.
    x += 10
    return x
  return xPlus

f1 = f()
f2 = f()
print(f1())
print(f1())
print(f1())
print(f2())
