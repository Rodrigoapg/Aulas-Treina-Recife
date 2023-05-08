'''EX23 apostila'''

menorpeso = 99999   #calcular menor numero entre os digitados

while True:
    p = float(input('Digite o seu peso:'))
    if p > 200: break
    if p < menorpeso : menorpeso = p   #calcular menor numero entre os digitados

print('O menor peso é:', menorpeso)
   

        
