name = 'josohyun'
age = 34

print('{0:^15}'.format(name)) #15자리 맞춰서 중앙정렬
print('{0:<15}'.format(name)) #왼쪽 정렬
print('{0:>15}'.format(name)) #오른쪽 정렬

print('{0:#^15}'.format(name)) #샵으로 나머지 공간 채우기
print('{0:0<15}'.format(name)) #0으로 나머지 공간 채우기
print('{0:!>15}'.format(name)) #!로 정렬 후 나머지 공간 채우기

print(f'제 이름은 {name}입니다. 제 나이는 {age}입니다.') #f문자열 포맷팅 기능, 3.6이상 버전에서 실행