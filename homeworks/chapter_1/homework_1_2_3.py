wrd = input()
new_wrd = []
a = []
for i in wrd:
    if i.isupper():
        new_wrd.append(wrd.index(i))
        break
for i in range(len(wrd)):
    if wrd[i].isdigit() and not(wrd[i+1].isdigit()):
        new_wrd.append(i+1)

a.append(wrd[new_wrd[0]:new_wrd[-1]+1:3])
a.append('.')
print(*a, sep='')
