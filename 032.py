#list 리스트 순서를 가지는 object들의 집합 리스트 기초
l = [100, 200, 300, 400]
print(l[3])
#print(자료형[index]) <- indexing 인덱싱
print(l[0:2])
#print(자료형[start:stop:step]) <- slicing 슬라이싱
l[0] = 1000
print(l)
l[0:2] = [3000, 3000]
print(l)
print(l[::-1]) #start와 stop을 생략하고 -1씩 출력하니까 역순으로 출력됨
print(l + l)
print(l * 3)
del l[0]
print(l)
l[0:1]= []
print(l)