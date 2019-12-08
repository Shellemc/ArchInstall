from os import popen

baner = """

\033[1;92m


			██████╗  █████╗ ██████╗ ████████╗██╗████████╗██╗ ██████╗ ███╗   ██╗███████╗
			██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██║╚══██╔══╝██║██╔═══██╗████╗  ██║██╔════╝
			██████╔╝███████║██████╔╝   ██║   ██║   ██║   ██║██║   ██║██╔██╗ ██║███████╗
			██╔═══╝ ██╔══██║██╔══██╗   ██║   ██║   ██║   ██║██║   ██║██║╚██╗██║╚════██║
			██║     ██║  ██║██║  ██║   ██║   ██║   ██║   ██║╚██████╔╝██║ ╚████║███████║
			╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝
                                                                           

\033[0m




"""

part = ['fdisk -l | sed -n 1p | cut -d: -f2 | cut -d, -f1 | tr -d a-zA-Z" "']
nome = ["fdisk -l | sed -n 1p | grep '/dev/...' | sed 's/.*\\/dev\\///g' | sed 's/\\:.*//g'"]
raiz = [f'echo "{part}" - 2 | bc']

v = popen(f'echo n; echo p; echo; echo; echo "+${raiz}""G";echo w) | fdisk /dev/${nome}').read()
v1 = popen(f'echo n; echo p; echo; echo; echo "+200""M";echo w) | fdisk /dev/${nome}').read()
v2 = popen(f'echo n; echo p; echo; echo; echo; echo t; echo; echo 82; echo w) | fdisk /dev/${nome}').read()

#funcao responsavel para criar as partiçoes no sistema que sera instalado
def criar_particao():
    for a, b, c in zip(part, nome, raiz):
        print('Criando partições, Por favor aguarde!')
        popen('clear').read()
        popen(a, b, c).read()
