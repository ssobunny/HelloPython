#재귀함수
def f(n):
  if n > 1:
    return n * f(n-1)
  else:
    return 1

print(f(5))
'''
f(5) 5*f(4) 5*24
f(4) 4*f(3) 4*6
f(3) 3*f(2) 3*2
f(2) 2*f(1) 2*1
f(1) 1
'''