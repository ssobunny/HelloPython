#list, dict, set의 인덱스를 붙이고 싶을 때
name = ['a', 'b', 'c']
for i in enumerate(name):
  print(i)

x = [(1, 2, (10, 20)), (3, 4, (30, 40)), (5, 6, (50, 60))]
for (i, j, (k, z)) in x:
  print(i, j, k, z)