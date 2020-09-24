def s(key):
  return {
    'one':1,
    'two':2,
    'three':3,
    'foru':4,
  }.get(key, 'Not Found')

print(s('one'))
print(s('five'))