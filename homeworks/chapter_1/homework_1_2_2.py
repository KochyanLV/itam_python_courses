a = []
while True:
    inp = input().split()
    if not inp: break
    a.append(inp)
# чтобы закончить ввод, введите пустую строку
ochno, zaochno, unknown = 0, 0, 0

for i in a:
    if i.count('True') + i.count("False") == 1:
        if i.count('True') == 1:
            ochno += 1
        else:
            zaochno += 1
    elif i.count('True') + i.count("False") > 1:
        if i[3] == 'True':
            ochno += 1
        if i[3] == 'False':
            zaochno += 1
        else:
            unknown += 1
print(ochno, zaochno, unknown)
