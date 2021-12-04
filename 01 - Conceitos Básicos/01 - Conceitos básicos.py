# Permite uma sentença em duas linhas
from decimal import Decimal, getcontext
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
4//3  # Divisão inteira
2 ** 3  # 2 elevado a 3
2 % 3  # Resto da divisão

aM = 1
bM = aM  # Copia o valor e não a referência

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
True ^ False  # xor bit a bit

binario = 0b01101
hexadecimal = 0xFF
octal = 0o770
-4
+4

variavel_ternaria = True
# A primeira é false e a sengunda verdadeiro
('Parte1', 'Parte2')[variavel_ternaria]
'Parte1' if variavel_ternaria else 'Parte2'  # A mesma coisa

lista2 = [1, 2, 'nome']
'nome' in lista2
1 not in lista2

# objeto é passado por referência mas valores são passados por valor

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

5.0.is_integer()  # Dá verdadeiro
abs(-2)  # Absoluto
print(1.1 + 2.2)

getcontext().prec = 30
print(Decimal(1.1) + Decimal(2.2))
dir(Decimal)

nome = 'nome'
print(nome[0])

# nome[0] = 'P' ERRO! Não permite atribuição de uma parte da string. string é imutável

print("D'água" == 'D\'água')
nome2 = 'Teste "2"'

doc = """Texto
de
multiplas
linhas"""
# Também serve '''

doc = 'Texto\nde\nmultiplas \
linhas'
# Lembrando que o \ permite quebrar a linha

acesso = 'João Antônio'
print(acesso[0])  # Acessa o primeiro
print(acesso[6])  # acessa o indice
print(acesso[-3])  # acessa de trás pra frente

# intervalos
print(acesso[4:])  # Pega do 4 em diante
print(acesso[-5:])  # começa de trás pra frente 5 casas
print(acesso[:3])  # intervalo 0,1,2 mas não inclui o 3
print(acesso[2:7])  # Mostra o intervalo de 2 até o 6. O 7 não entra

numeros = '0123456789'
print(numeros[::])  # mostra tudo
print(numeros[::2])  # mostra de 2 em 2, no caso só os pares
# mostra de dois em dois só que começando no 1, no caso mostra os ímpares
print(numeros[1::2])
print(numeros[::-1])  # inverte a string
print(numeros[::-2])  # percorre de 2 em dois com a string invertida

frase = 'Python é legal'
print('py' not in frase)  # o in procura na string
# .lower() transforma tudo em minusculo e .upper() em maiusculo
print('py' in frase.lower())
print(len(frase))  # Mostra o tamanho
print(frase.split())  # separa por espaços
# separa por um caractere especifico. O caractere não entra
print(frase.split('é'))


lista3 = [1, 5.2, True, 'Teste']

lista3.append('Adiciona um elemento')
lista3.remove(5.2)  # procura o 5.2 e remove
lista3.reverse()  # iinverte a lista, diferente da string ela muda mesmo
lista3.index('Teste')
lista3[2]
1 in lista3
lista3[-1]  # acessa o último
# intervalo
print(lista3[1:3])  # mostra do 1 ao 2. não inclui o 3
print(lista3[1:-1])  # vai do 1 até o -1 sem incluir o -1(que é o último)
print(lista3[1:])
print(lista3[:-1])
print(lista3[:])
print(lista3[::2])  # de dois em dois
print(lista3[::-1])  # inverte
del lista[2]  # deleta um elemento específico
print(lista)
del lista[1:3]  # deleta um intervalo
print(lista)

# Tupla é uma lista imutável

tupla = ()
tupla = ('um',)  # pra não confundir com ()
tupla = (1, 2, 3, 4, 5, 6, 7, 8, 9)

# Dicionário é um map

dicionário = {'chave': 'valor', 'lista': ['lista', 'lista'], 1:'A chave pode ser um tipo primitivo'}
print(dicionário['lista'][1])
print(dicionário.keys())
print(dicionário.values())
print(dicionário.items())
print(dicionário.get('chave'))

dicionário.pop(1) #Remove dá pra usar del também
dicionário.update({'chave': 'valor2'}) #altera
print(dicionário.items())

#conjunto (set não é indexado e não aceita repetição

conjunto = {'1','1','2','3'}
conjunto2 = set('111233') 
print(conjunto == conjunto2)
'3' in conjunto2

c1 = {1,2}
c2 = {2,3}
c1.union(c2)
c1.intersection(c2)
c1.update(c2) #União que modifica c1
c2 <= c1 #é subconjunto, está contido

{1,2,3} - {2} #tira o 2

c1 -= {2} #Operadores funcionam


#Interpolação

nome, idade, peso = 'Carlos', 30, 98.937

print('Nome: %s\nIdade: %d\nPeso: %.2f\n' % (nome, idade, peso))
print('Nome: {0}\nIdade: {1}\nPeso: {2}\n'.format(nome, idade, peso))
print(f'Nome: {nome}\nIdade: {idade}\nPeso: {peso}\n')

from string import Template

temp = Template('Nome: $nome \nIdade: $idade \nPeso: $pesoX\n')
print(temp.substitute(nome=nome, idade=idade, pesoX=peso))
