n = int(input())
n2 = input()
c = 0  # исходные данные

for i in n2:  # проверим есть ли 0
    if i == '0':
        c += 1


if c > 0:  # если счетчик 0, значит 0 нет
    print('YES')
else:
    print('NO')
