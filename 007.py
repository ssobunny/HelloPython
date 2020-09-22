#변수의 타입
a = 10  #a가 10을 가리킨다. int
b = 10.1 #float
c = '''josohyun''' #str
d = True #bool(True, False)
e = [100, 200, 300] #list
f = (100, 200, 300) #tuple
g = {'one':1, 'two':2} #dict
h = {100, 200, 300, 400} #set

print(type(a), type(b), type(c), type(d), type(e))
print(type(f), type(g), type(h))
print(a + a)
print(b + b)
print(c + c)
print(c.isalpha())
'''
1. 공간활용
2. 용도에 맞게 사용, 유용한 기능 사용
3. 변수와 값은 모두 존재함
'''
print(dir(c))
'''
dir은 안에 들어가 있는 object가 그 타입일 수 있는 이유(속성)와 
그 타입에 사용할 수 있는 유용한 기능(메서드)를 보여주는 함수
'''
