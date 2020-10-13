#max, min, sum
x = [100, 200, 300, 400]
print(max(x))
print(min(x))
print(sum(x))
print('----------')
a= [1, 2, 3]
b = 'DEF'
c = 'GHI'
print(list(zip(a, b, c))) #zip은 그냥 쓰면 안되고 list나 tuple로 변환시켜야 활용할 수 있다.
for i in zip(a, b):
  print(i)
print('----------')
def sohyun(x):
  return x * 2

print(list(map(sohyun, [1, 2, 3]))) #각각 제곱이 되는 수가 출력됨
print(list(map(sohyun, 'ABC')))
print(list(map(lambda x : x ** 2, [1, 2, 3]))) #제곱시킴