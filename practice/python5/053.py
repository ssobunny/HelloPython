class Car(object):
  def __init__(self):
    print('인스턴스가 생성되었습니다.')
  def addkinds(self, name):
    self.kinds = []
    self.kinds.append(name)
  maxSpeed = 300
  maxPeople = 5
  def move(self, x):
    print(x, '의 스피드로 움직이고 있습니다.')
  def stop(self):
    print('멈췄습니다.')

k3 = Car()
print(dir(k3))

'''
__init__ : 생성자, 인스턴스로 생성되었을 때 실행됨
del : 소멸되었을 때 실행됨, 소멸자
add : + 연산 (연산자 오버로딩)
or : bit단위 OR 연산
repr, str : 클래스를 프린트 했을 경우 출력해주는 문자열
call : 함수를 호출, 함수 호출했을 때 실행됨
getattr : 속성 가져오기
setattr : 속성 할당하기
delattr : 속성 제거
dataattribute : 속성 가져오기
getitem : indexing, slicing, 반복을 위해 사용
setitem : index, slice된 값을 가져오기 위해 사용
delitem : index, slice된 값을 삭제하기 위해 사용
bool
len
lt, gt, le, ge, eq, ne : >, <, <=, >=, ==, !=
radd : 오른쪽 기준 연산자
iadd :  += -=
iter, next : 반복을 위해 사용
contains : in 멤버가 있는지 알기 위해 씀
index : 정수값을 나타냄, 순서 X
enter, exit : with (contents manager)
get, set, delete : .찍고 사용함 
new : init 이전에 객체 생성시 사용
'''