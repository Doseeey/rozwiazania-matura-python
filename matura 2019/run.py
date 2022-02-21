file = open('przyklad.txt', 'r')
dane = file.readlines()

'''ZADANIE 1'''

def create_three_list():
    lista = []
    x = 1
    while x < 100000:
        lista.append(x)
        x *= 3
    return lista

T = create_three_list()

i = 0
for num in dane:
    if int(num) in T:
        i += 1
    else:
        continue
print(i)

'''ZADANIE 2'''

def power(x):
    if x == 0:
        return 1
    else:
        return(x*power(x-1))

def check_power(num):
    res = 0
    for cyf in num:
        res += power(int(cyf))
    if res == int(num):
        return num


for num in dane:
    x = check_power(num[:-1])
    if x != None:
        print(x)


'''ZADANIE 3'''

def nwd(a, b):
    while b:
        a, b = b, a%b
    return a

def check_long(x):
    nl = []
    res = {}
    r = 2
    t = int(x[0])
    for n in x[1:]:
        if n == t:
            nl.append(n)
            r += 1
            t = n
        else:
            res[int(r)] = '{} {}'.format(t, nl)
            r = 2
            t = n
            nl = []
    return max(res), res[max(res)]


t = int(dane[0])

nwd_list = []
no1_list = []

for num in dane:
    tfunc = nwd(t,int(num))
    if tfunc > 1:
        no1_list.append(tfunc)
    nwd_list.append(tfunc)
    t = int(num)

print(check_long(no1_list))