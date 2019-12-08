from os import popen
from time import sleep

banner = """

      \033[1;92m

                  

                                          ████████╗ ██████╗  ██████╗ ██╗     ███████╗
                                          ╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██╔════╝
                                             ██║   ██║   ██║██║   ██║██║     ███████╗
                                             ██║   ██║   ██║██║   ██║██║     ╚════██║
                                             ██║   ╚██████╔╝╚██████╔╝███████╗███████║
                                             ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝
                                    
\033[0m
"""
print(banner)

# comandos que serão passado para ser executado no sistema
comandos = ['loadkeys br-abnt2', 'ping -c1 www.google.com', 'timedatectl set-ntp true', 'mkfs.ext4 /dev/sda1', 'mkswap /dev/sda3', 'mkfs.ext4 /dev/sda2', 'swapon /dev/sda3',
            'mount /dev/sda1 /mnt', 'mkdir /mnt/boot', 'mount /dev/sda2 /mnt/boot', 'pacstrap /mnt/base linux linux-firmware',
            'genfstab -U /mnt >> /mnt/etc/fstab', 'ln -sf /usr/share/zoneinfo/Brazil/East /etc/localtime',
            'echo "pt_BR.UTF-8 UTF-8" >> /etc/locale.gen', 'echo "LANG=pt_BR.UTF-8" > /etc/locale.conf', 'local-gen',
            'echo "KEYMAP=br-abnt2" > /etc/vconsole.conf', 'echo "arch" > /etc/hostname', 'echo -e "127.0.0.1\\tlocalhost\\n::1\\tlocalhost\\n127.0.1.1\\tarch.linux\\tarch\\n" > /etc/hosts',
            'mkinittcpio -p linux', 'pacman -S grub --noconfirm', 'grub-install --target=i386-pc --recheck /dev/sda',
            'pacman -S os-prober --noconfirm', 'grub-mkconfig -o /boot/grub/grub.cfg', 'pacman -S dhcpcd --noconfirm',
            'systemctl enable dhcpcd']

# mensagem de cada comando acima
msg = ["Configurando o teclado....",
       "Testando a internet.......",
       "Checando o relógio........",
       "Formatando o root.........",
       "Formatando a swap.........",
       "Formatando o boot.........",
       "Ativando a swap...........",
       "Montando o root em /mnt...",
       "Criando /mnt/boot.........",
       "Montando sda2 em boot.....",
       "Instalando o básico.......",
       "Gerando a /et/fstab.......",
       "Configurando o horário....",
       "Definindo o idioma........",
       "Gerando o idioma..........",
       "Configurando o idioma.....",
       "Configurando o teclado....",
       "Definindo o hostname......",
       "Definindo virtual host....",
       "Copiando a img do Kernel..",
       "Baixado o grub............",
       "Instalando o grub na MBR..",
       "Adiconando opções ao grub.",
       "Configurando o grub.......",
       "Instalando o dhcpcd.......",
       "Habilitando o dhcpcd......"
       ]


def tools():
    for mensagem, comando in zip(msg, comandos):
        sleep(3)  # dar uma pausa de 3 segundos para cada comando ser executado
        print(f'[+] - {mensagem} -> {popen(comando).read()}')

