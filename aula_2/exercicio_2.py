BANDO_DE_DADOS = []

class InvalidEmailError(Exception):
	pass

class InvalidAgeError(Exception):
	pass

class InvalidUsuarioCadastradoError(Exception):
	pass

def cadastrar_usuario():
	email = input('Digite seu email: ')
	if '@' not in email:
		raise InvalidEmailError
		#raise Exception({
			#'status_code': 400,
			#'message': 'Email inválido'

		#})

	idade = int(input('Digite sua idade: '))
	if idade <= 0:
		raise InvalidAgeError
		#raise Exception({
			#'status_code': 400,
			#'message': 'idade menor do que zero'

		#})
	return idade
	
	# Recebe os dados do novo usuário
	usuario = {
		'email': input('Digite seu email: '),
		'idade': input('Digite sua idade: ')
	}
	if '@' not in usuário['email']:
		raise Exception({
			'status_code': 400,
			'message': 'Email inválido'
		})

	# Encontra possíveis erros na criação do usuário


	# Retorna o usuário criado
	return {
		'email': email,
		'idade': idade
	}

def cadastrar_usuario(usuario):
	for usuario_cadastrado in BANCO_DE_DADOS:
		if usuario_cadastrado['email'] == usuario['email']:
			raise InvalidUsuarioCadastradoError
		BANCO_DE_DADOS.append(usuario)
		# Verificar se o usuario já existe no banco
def verificar_senha(usuario):
	senha = input('Digite a senha: ')
	if usuario['senha'] != senha:

try:
	usuario = receber_novo
	cadastrar_usuario()
	print('Usuário cadastrado com sucesso')
except InvalidEmailError as err:
	print('Email invalido')

except InvalidAgeError as err:
	print('Idade inválida')
#except Exception as err:
	#err = err.args[0]
	#print('Código do erro: {}'.format(err['status_code']))
	#print('Mensagem: {}'.format(err['message']))