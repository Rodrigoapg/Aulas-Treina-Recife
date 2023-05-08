'''EX 28 apostila'''

T = int(input('Digite a quantidade de termos:'))

a = 1
b = 1
print(a)
print(b)

for Te in range(2, T , 1):
    c = a + b
    print(c)
    a = b
    b = c

