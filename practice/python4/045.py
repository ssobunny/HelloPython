x = 10
y = '10'
z = 10.1
print(x + x)
print(x + int(y))
print(y + y) #concat
#print(x + y) 형이 다른데 연산이 된다? float와 int형만 됨
print(type(x + z))
#숫자 > 문자
print(chr(65))
print(chr(97))
#문자 > 숫자
print(ord('A'))
print(chr(ord('A') + 1))
print(chr(66))
print(ord('가'))
