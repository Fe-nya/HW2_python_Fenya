n = int(input())
c = 0  # счетчик
a = 0  # сумма чисел

while n != 0:
    c += 1
    a += n
    n = int(input())

print(a/c)  # среднее арифметическое
