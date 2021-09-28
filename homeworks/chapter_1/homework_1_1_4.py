b = input().split() #введите данные через пробел
a = list(map(int, b))
c1, c2, c3 = 0, 0, 0
for i in a:
    if i < 0:
        c1 += 1
    if i > 8:
        c2 += 1
    if i % 2 == 0:
        c3 += 1
print(c1, c2, c3)
