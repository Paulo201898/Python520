#!/usr/bin/python3

import banco

# print(banco.lista_de_usuarios)

# exercício 1:
# Imprima somente os usuários
# cujos emails contenham as letras:
# 'a' ou 'k' ou 'm' ou 'l'
# e cujas idades sejam
# maior que 30 e menor que 40

# Dica de exercício

# Condições ou
#if 2 < 4 or 5 < 10:
#    print('Condição OU')

# Condição E
#if 2 < 4 and 5 < 10:
#    print('Condição AND')

# Testar se uma letra está em uma string
#if 'P' in 'Paulo'.lower():
#    print('Paulo tem P')

# Obs: A Função lower() converte uma string
# para letra minuscula
# print('PAULO'.lower()) # Imprime 'Paulo' tudo minusculo

# condicao_1 = 'P' in 'Paulo'
# condicao_2 = 20 < 40

#if condicao_1 and condicao_2:
#    print('Opaa')


for usuario in banco.lista_de_usuarios:
	if usuario['idade'] < 30:
		print(usuario['idade'])

		email = usuario['email'].lower()
		idade = usuario['idade']

		condicao_1 = 'a' in email
		condicao_1 = condicao_1 or 'k' in email
		condicao_1 = condicao_1 or 'm' in email
		condicao_1 = condicao_1 or 'l' in email

		condicao_2 = idade > 30 and idade < 40

		if condicao_1 and condicao_2:
			print(usuario)