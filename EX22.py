'''EX22 apostila'''

soma = 0
c = 0
qpar = somapar = 0
while True:
    N = float(input('Digite um número:'))
    if N == 999: break
    soma = soma + N
    c = c + 1
    resto = N % 2
    if resto == 0:
        qpar = qpar + 1
        somapar = somapar + N #isso é para descobrir se o número é par





print('A quantidade de números digitados foi:', c)
print('A quantidade da soma foi:', soma)

mediapar = somapar / qpar

print('A media dos pares foi:', mediapar)
