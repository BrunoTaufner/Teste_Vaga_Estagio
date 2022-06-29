palavra, anagrama = input().split(', ')
palavra = list(palavra)
anagrama = list(anagrama)
i = 0
while i < len(palavra):
    j = 0
    while j < len(anagrama):
        if palavra[i] == anagrama[j]:
            palavra.pop(i)
            anagrama.pop(j)
            i = -1
            break
        j += 1
    i += 1

if len(anagrama) == 0 and len(palavra) == 0:
    print('true')
else:
    print('false')
