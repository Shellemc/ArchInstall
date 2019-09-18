from os import system

part = ['fdisk -l | sed -n 1p | cut -d: -f2 | cut -d, -f1 | tr -d a-zA-Z" "']
nome = ["fdisk -l | sed -n 1p | grep '/dev/...' | sed 's/.*\\/dev\\///g' | sed 's/\\:.*//g'"]
raiz = [f'echo "{part}" - 2 | bc']

print(f'raiz: {raiz} | part: {part}')

#lista_comandos = ['dir', 'dir', 'dir' ]
#lista_mensagens = ['primeiro', 'segundo', 'terceiro']
def t ():
	for comandos in lista_comandos:
		print('\n')
		print("=" * 70)
		print('O comando passado foi: {}\n'.format(comandos))
		print("=" * 70)
		system(comandos)

t()
#def criar_part():
