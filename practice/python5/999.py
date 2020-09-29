'''
class Employee:
  pass #attribute나 method가 없을 때 입력
'''
class Employee:
  #생성자
  def __init__(self, first, last, pay):
    self.first = first
    self.last = last
    self.pay = pay
    self.email = first + '.' + last + '@company.com'

  def fullname(self):
    return '{} {}'.format(self.first, self.last)


emp_1 = Employee('Corey', 'Schafer', 50000) #인스턴스
emp_2 = Employee('Test', 'User', 60000) #인스턴스

#print(emp_1)
#print(emp_2)

print(emp_1.email)
print(emp_2.email)

print(emp_2.fullname())
print(Employee.fullname(emp_1))
#emp_1.fullname()과 같음. fullname메서드에 self가 포함되는 이유는 self에 emp_1을 넣는 것과 동일한 역할을 하기 때문이다.