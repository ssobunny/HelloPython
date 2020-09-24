s = 'djdj;ksjdhfj;iyuehf;ssdiytge'
#print(set(s))
#중복을 허락하지 않는 것만 추출 가능 set으로 형변환해서 연산하면 됨
print(len(set(s)))
count = 0
for i in set(s):
  count += 1
  print(i)
print(count)