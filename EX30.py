'''EX30 apostila'''

menor = 9999
Qm = sAm = 0

for x in range(1,11,1):
    sexo = input('Digite seu sexo:')
    altura = float(input('Digite sua altura:'))
    if altura < menor:
        menor = altura
    if sexo == 'm':
        Qm = Qm + 1
        sAm = sAm + altura

print('A menor altura foi:', menor)
media = sAm / Qm
print('A media da altura dos meninos foi:', media)


    
    
    
