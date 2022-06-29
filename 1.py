meias = [10, 20, 10, 20, 10, 30, 50, 10]
pares = []
i = 0
while i < len(meias):
    j = 1
    while j < len(meias):
        if j != i and meias[i] == meias[j]:
            pares.append([meias[i], meias[j]])
            meias.pop(i)
            meias.pop(j - 1)
            i = -1
            break
        j += 1
    i += 1

for par in pares:
    print(par)

print(len(pares))
