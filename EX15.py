'''EX15 renda_casal
entradas: calcular (IR), input (RH) e (RM),
processamento: RC = RH + RM
saídas: mostrar na tela renda conjunta(RC), percentual do imposto, valor do (IR) calculado
e renda liquida(RLQ)'''


RH = float(input('Digite quanto é a renda do homem: '))
RM = float(input('Digite quanto é a renda da mulher: '))

RC = RH + RM



if RC <= 900.00:
    IR = RC * (0 / 100)
    print('A porcentagem do IR foi 0%.')
    print('O imposto de renda é:', IR)
    
if RC >= 900.01 and RC <= 1500.00:
    IR = RC * (10 / 100)    
    print('A porcentagem do IR foi 10%.')
    print('O imposto de renda é:', IR)    

if RC >= 1500.01 and RC <= 2500.00:
    IR = RC * (15 / 100)
    print('A porcentagem do IR foi 15%.')
    print('O imposto de renda é:', IR)
    
if RC > 2500.00:
    IR = RC * (25 / 100)
    print('A porcentagem do IR foi 25%.')
    print('O imposto de renda é:', IR)

RLQ = RC - IR


print('A renda conjunta é:', RC)
print('O salário líquido é:', RLQ)

