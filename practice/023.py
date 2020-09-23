#continue 바로 다음 루프로 넘어가게 함
for i in range(101):
     if i % 2 == 0:
        continue
     print(i)
     if i > 50:
        break
else:
    print('good job')