#튜플 기초, 변경 불가능해서 append 불가능
t = (100, 200, 300, 400)
#출력할 때는 붙일 수 있음
print(t + t)
print(t * 3)
#인덱스가 있어서 인덱싱 가능
print(t[0])
print(t[1])
#슬라이싱도 가능
print(t[1:3])