#리스트 메서드
l = [100, 200, 300, 400]
print(type(l))
print(dir(l))
l.append(500)
print(l)
l.append(500) #마지막에 집어넣는다.
print(l)
print(l.count(500))
l.extend([100, 200, 10, 20]) #같은 자료형을 붙여줘야함. 리스트니까 리스트를 붙인다.
print(l)
print(l.index(200))
l.insert(3, 10000)
print(l)
l.pop(2) #마지막에 있는걸 꺼낸다. index값이 들어감
print(l)
l.remove(200) #값을 꺼냄, 처음 만나는 값만 꺼냄
print(l)
l.reverse()
print(l)
l.sort() #정렬
print(l)
