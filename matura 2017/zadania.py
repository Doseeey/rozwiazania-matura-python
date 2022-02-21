file = open('przyklad.txt', 'r')
dane = file.readlines()

'''ZADANIE 1'''

najw = 0
najm = 255

for word in dane:
    x = list(word.split())
    for num in x:
        if int(num) > int(najw):
            najw = int(num)
        if int(num) < int(najm):
            najm = int(num)

print(najw, najm)

'''ZADANIE 2'''

sym = 0

for word in dane:
    x = list(word.split())
    for i in range(len(x)):
        if x[i] != x[-(i+1)]:
            sym += 1
            break

print(sym)

'''ZADANIE 3'''



'''ZADANIE 4'''

n = ''
liczba = 1
max = 0

for pos in range(319):
    for i in range(len(dane)-1):
        col = list(dane[i].split())
        pix = col[pos]
        if n == '':
            n = int(pix)
            continue
        if int(pix) == int(n):
            liczba += 1
        else:
            if max < liczba:
                max = liczba
                liczba = 1
                n = ''
            else:
                liczba = 1
                n = ''
                
print(max)