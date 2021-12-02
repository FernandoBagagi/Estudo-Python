# Permite uma sentença em duas linhas
1 \
    + 2

# Tipos Primitivos

booleano = True | False
inteiro = 1
real = .2 + 1. + 2.1
string = 'Apas simples'
string2 = "Aspas duplas"
# Pode misurar aspas simples e duplas mas não é recomendado
print('Você é ' + 3 * "muito " + 'legal')
# print(3 + '3') -> Ambiguidade
lista = [1, 2, 3]
dicionário = {'chave': 'valor', 'numero': 1.7, 'verdade': False}
nulo = None
"""
Comentário
de
multiplas
linhas
"""
'''
outra
forma
'''
2+3
2-5
2*8
2/7
4//3 #Divisão inteira
2 ** 3 #2 elevado a 3
2%3 #Resto da divisão

aM = 1
bM = aM #Copia o valor e não a referência

2 > 2
2 >= 2
2 < 2
2 <= 2
2 != 2
2 == 2
aM += 5
aM -= 5
aM *= 5
aM /= 5
aM //= 5
aM %= 5
aM **= 5

True or False
True and True
not True
not 0
not 1
not not False

True & False
True | False
True ^ False #xor bit a bit

binario = 0b01101
hexadecimal = 0xFF
octal = 0o770
-4
+4

variavel_ternaria = True
('Parte1' , 'Parte2')[variavel_ternaria] #A primeira é false e a sengunda verdadeiro
'Parte1' if variavel_ternaria else 'Parte2' #A mesma coisa

lista2 = [1, 2, 'nome']
'nome' in lista2
1 not in lista2

#objeto é passado por referência mas valores são passados por valor

a1 = 1
a2 = a1
a3 = 1

a1 is a2
a1 is a3

l1 = [1, 2, 3]
l2 = l1
l3 = [1, 2, 3]

l1 is l2
l3 is l1

__builtins__.type(l1)
__builtins__.print('Exemplo')

conversão = 1
print(conversão)
print(type(conversão))
conversão = float(conversão)
print(conversão)
print(type(conversão))
conversão = str(conversão)
print(conversão)
print(type(conversão))
conversão = bool(conversão)
print(conversão)
print(type(conversão))

5.0.is_integer() #Dá verdadeiro
abs(-2) #Absoluto
print(1.1 + 2.2)

from decimal import Decimal, getcontext
getcontext().prec = 30
print(Decimal(1.1) + Decimal(2.2))
dir(Decimal)
