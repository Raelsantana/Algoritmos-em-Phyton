#Declarando as duas variáveis que serão digitadas pelo usuário
n1 = float(input('Digite um número: '))
n2 = float(input('Ditige outro número: '))

#Declarando as operações aritméticas
soma = n1 + n2
sub = n1 - n2
div = n1 / n2
mult = n1 * n2
potencia = n1 ** n2
divisaointeira = n1 // n2
restodiv = n1 % n2

#Imprimindo os resultados
print(f'A soma dos números {n1} e {n2}, tem como resultado: {soma}')
print(f'A subtração dos números {n1} e {n2}, tem como resultado: {sub}')
print(f'A multiplicação entre os números {n1} e {n2}, tem como resultado: {mult}')
print(f'A divisão dos números {n1} e {n2}, tem como resultado: {div:.2f}')
print(f'A pontência do número {n1} pelo {n2}, tem como resultado; {potencia:.2f}')
print(f'A divisão inteira de {n1} por {n2}, tem como resultado: {divisaointeira}')
print(f'O resto de divisão de {n1} por {n2}, tem como resultado: {restodiv}')

