#MRO : 메서드 검색 순서
class One : x = 1
class Two(One): pass
class Three(One) : x = 2 #변수 재정의
class Four(Two, Three) : pass

i = Four()
print(i.x)

