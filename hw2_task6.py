n = int(input())
a = 1  # вспомогательная переменная
c = 1  # сумматор

for i in range(1, n + 1):
    for j in range(2, i + 1):
        a *= j
    c += 1 / a  # добавляем факториал

print(round(c, 5))  # выводим результат
