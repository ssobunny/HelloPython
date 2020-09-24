a = 13
#2진법
print(bin(a))
#8진법
print(oct(a))
#16진법
print(hex(a))
#bin, oct, hex를 이용해 진법을 바꾸면 string이고 직접 대입해서 넣으면 int이다.
print(type(bin(a)))
print(type(oct(a)))
print(type(hex(a)))

x = 0b1101
y = 0o15
z = 0xd

print(type(x), y, z)
print(bin(a)[2:].replace('1', '#').replace('0', '!')) #중요