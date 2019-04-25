import banco

TOLERANCIA = 15

acertos = 0

while acertos < 3:

	idade = ''

	for usuario in banco.lista_de_usuarios:
		idade = usuario['idade']
		numero = input('Digite: ')
		numero = int(numero)
		if numero in range(idade - TOLERANCIA, idade + TOLERANCIA):
			acertos = acertos + 1
		print('Você já acertou: ' + str(acertos))
		if acertos == 3:
			break
print('Ganhou o jogo')

exit()

condicao = True

while condicao:
	condicao = False

print('Opa')

import banco


exit()

import banco

acertos = 0

while acertos < 3:

	for usuario in banco.lista_de_usuarios:
		idade = usuario['idade']

		# pedir para o usuario digitar um numero
		# verificar se este numero esta no range(idade -5, idade + 5)
		# se estiver, incrementa o numero de acertos

	# imprime que o jogo acabou