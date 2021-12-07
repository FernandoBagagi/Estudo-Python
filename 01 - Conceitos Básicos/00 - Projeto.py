# -*- coding: utf-8 -*-
import math
import sys

print(f'pi = {math.pi}')
PI = 3.14159
raio = float(input('Digite o valor do raio em cm: '))

print(f'A área é {PI * raio **2}cm^2 em outra precisão {math.pi * raio **2}cm^2')
print(f'Erro {math.pi * raio **2 - PI * raio **2}')

print(f'Argumentos {sys.argv[0]}') #selecionar e apertar ctrl+alt+n executa só aquele trecho
sys.exit(0)