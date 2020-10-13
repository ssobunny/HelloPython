file = open('sample.txt', 'r') #r : read, a : append, w : 지우고 다시 씀
'''
file.write('hello world')
file.write('\n')
file.write('hello world')
file.close()
'''
#print(dir(file))
print(file.readlines())
#print(file.readline())
#print(file.readline())
#print(file.read())
file.close()