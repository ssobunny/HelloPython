class Test:
  def __init__(self, testdata):
    #print('self1', self)
    self.data = testdata
    #print('testdata', testdata)
  def __sub__(self, other):
    #print('self', self)
    #print('other', other)
    return Test(self.data + other)

x = Test(5)
print(x.data) #클래스 생성자만 호출함
y = x.__sub__(2)
'''
y = x - 2 와 같은 의미임
원래 __sub__ 메서드는 빼기의 의미인데 더하기를 return해서 오버로딩함
'''
print(y.data) #7