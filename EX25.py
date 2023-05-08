'''EX25 população'''


Pa = float(input('Digite a população do pais A:'))
Pb = float(input('Digite a população do pais B:'))

anos = 0
while Pa < Pb:
    Pa = Pa + ( Pa * 3 / 100)
    Pb = Pb + ( Pb * 1.5 / 100)  #calcular porcentagem é assim
    anos = anos + 1
    


print('Foram necessários:',str(anos)+' anos.')



    
    
