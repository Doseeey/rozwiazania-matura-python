file = open('sygnaly.txt', 'r')
data = file.readlines()

'''ZADANIE 1'''
i = 39
while i < 1001:
    x = data[i]
    print(x[9], end='')
    i += 40

print()
'''ZADANIE 2'''

i = 0
p = ''

for word in data:
    x = set(word)
    if len(x) > i:
        i = len(x)
        p = word

print(p[:-1], i-1)

print()
'''ZADANIE 3'''

def odleglosc(w):
    x = max(w)
    y = min(w)
    if ord(x) - ord(y) <= 10:
        print(w)

for word in data:
    odleglosc(word[:-1])

