#print('meu primeiro programa em python')
#a = 10
#b = 5

a = int(input('Entre com o primeiro valor:'))
b = int(input('Entre com o segundo valor:'))

soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b


#print(soma)
#print(subtracao)
#print(multiplicacao)
#print(divisao)

resultado = ('Soma: {soma}. \nSubtracao: {sub}. \nMultiplicacao: {multiplicacao}. \nDivisao: {divisao}.'.format(soma=soma, sub=subtracao, multiplicacao=multiplicacao, divisao=divisao))
print(resultado)

#pode se usar o print(type()) para saber o tipo de classe
#print('soma: ' + str(soma))

#voce consegue converter inteiro para string usando str()
#print('divisao: ' + str(divisao))

#x = 1
#soma2 = int(x) +1
#print(soma2)