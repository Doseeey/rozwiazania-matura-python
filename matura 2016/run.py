file = open("dane_6_1.txt")
dane = file.readlines()

'''ZADANIE 1'''

lista = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
k = 107

def szyfr(word):
    res = ''
    for let in word:
        i = lista.index(let)
        new_let = lista[(i+107)%len(lista)]
        res += new_let
    return res

for wd in dane:
    print(szyfr(wd[:-1]))

'''ZADANIE 2'''
from math import fabs

file = open("dane_6_2.txt")
dane = file.readlines()

lista = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def rev_szyfr(word, k):
    res = ''
    for let in word:
        i = lista.index(let)

        ind = (i-k) % len(lista)
        new_let = lista[int(fabs(ind))]

        res += new_let

    return res

for wd in dane:
    try:
        slowo, index = wd.split()
        print(rev_szyfr(slowo, int(index)))
    except:
        continue

'''ZADANIE 3'''

file = open("dane_6_3.txt")
dane = file.readlines()

lista = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def sprawdz_przesuniecie(a, b):
    l1 = a[0]
    i = lista.index(l1)
    l2 = b[0]
    for j in range(i, i+26):
        k = 0
        temp_let = lista[(lista.index(l1)+j)%len(lista)]
        if temp_let == l2:
            return k
        else:
            continue

def sprawdz_czy_szyfr(a, b, k):
    for let in a:
        i = lista.index(let)
        new_let = lista[(i + k) % len(lista)]

        letter_index = 0
        if new_let != b[letter_index]:
            return a
        else:
            letter_index += 1



for wd in dane:
    w1, w2 = wd.split()
    k = int(sprawdz_przesuniecie(w1, w2))
    print(sprawdz_czy_szyfr(w1, w2, k))


