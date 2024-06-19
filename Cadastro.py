#Faça um programa que receba o nome de um usuário e deseje boas vindas.

nome = str(input('Digite seu nome: '))
idade = int(input('Digite sua idade: '))
peso = float(input('Digite seu peso: '))

print(f'Seja Bem Vindo, {nome}!')
print(f'Sua idade é {idade}.')
print(f'Você está pesando {peso:.1f}Kg.')

#Função "input('')" é utilizada para receber dados do usuário.
