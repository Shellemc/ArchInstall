from os import popen

part = ['fdisk -l | sed -n 1p | cut -d: -f2 | cut -d, -f1 | tr -d a-zA-Z" "']
nome = ["fdisk -l | sed -n 1p | grep '/dev/...' | sed 's/.*\\/dev\\///g' | sed 's/\\:.*//g'"]
raiz = [f'echo "{part}" - 2 | bc']

#funcao responsavel para criar as partiçoes no sistema que sera instalado
def criar_particao():
    for a, b, c in zip(part, nome, raiz):
        print('Criando partições, Por favor aguarde!')
        popen('clear').read()
        popen(a, b, c).read()
