from os import system

part = ['fdisk -l | sed -n 1p | cut -d: -f2 | cut -d, -f1 | tr -d a-zA-Z" "']
nome = ["fdisk -l | sed -n 1p | grep '/dev/...' | sed 's/.*\\/dev\\///g' | sed 's/\\:.*//g'"]
raiz = [f'echo "{part}" - 2 | bc']

print(f'raiz: {raiz} | part: {part}')