#내장함수
print(abs(-1)) #절대값
print(all([1, 2, 3, 4, 5, 6, 7])) #모든 값이 True일 때 True
print(any([0, 0, 0, 1])) #하나만 True여도 True
print('1 ------------')
print(bool(''))
print(bool(' '))
print('2 ------------')
print(bool(1))
print(bool(0))
print('3 ------------')
print(chr(65)) #아스키코드표 참조
print(chr(97))
print('4 ------------')
print(ord('A'))
print(ord('a'))
print('5 ------------')
print(dict([('one', '1'), ('two', '2')]))
print('6 ------------')
print(float(10))
print(int(10.9)) #버림
print('7 ------------')
print(set('aaaabbccc')) #중복제거, 순서X
print(len(set('aaaabbccc'))) #중복제거해서 알파벳 세기