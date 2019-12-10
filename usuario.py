import os
import crypt

def criar_usuario(user, pwd):
	for linha in open('/etc/passwd').readlines():
		linha = linha.split(':')
		if linha[0] == user:
			print('Usuario %s já existe' % user)
			return
		cmd = 'useradd -p %s %s 2>/dev/null' % (crypt.crypt(pwd, '22'), user)
		output = os.popen((cmd).readline())
		print('Usuario %s criado com sucesso' % user)

nome_usuario = input('nome do usuario: ')
senha_usuario = input('senha do usuario: ')
criar_usuario(nome_usuario, senha_usuario)