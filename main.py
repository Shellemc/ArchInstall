from time import sleep
from configuracao import tools
from criar_particoes import criar_particao
import subprocess
import os
import sys


###########################################
"MENU PRINCIPAL DO PROGRAMA"
###########################################


def banner():
    ban = """

    \033[32m

		 █████╗ ██████╗  ██████╗██╗  ██╗    ██╗███╗   ██╗███████╗████████╗ █████╗ ██╗     ██╗
		██╔══██╗██╔══██╗██╔════╝██║  ██║    ██║████╗  ██║██╔════╝╚══██╔══╝██╔══██╗██║     ██║
		███████║██████╔╝██║     ███████║    ██║██╔██╗ ██║███████╗   ██║   ███████║██║     ██║
		██╔══██║██╔══██╗██║     ██╔══██║    ██║██║╚██╗██║╚════██║   ██║   ██╔══██║██║     ██║
		██║  ██║██║  ██║╚██████╗██║  ██║    ██║██║ ╚████║███████║   ██║   ██║  ██║███████╗███████╗
		╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝    ╚═╝╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚══════╝

	\033[0;0m

	\033[93m
	    [ 1 ] -> INSTALAR O SISTEMA
	    [ 0 ] -> SAIR DO PROGRAMA
	\033[0;0m
    """
    print(ban)


banner()

while True:
    opc = int(input('digite o número da opção desejada:'))
    if opc == 1:
        criar_particao()
        tools()

    elif opc == 2:
        print('saindo do programa...'.upper())
        exit()
