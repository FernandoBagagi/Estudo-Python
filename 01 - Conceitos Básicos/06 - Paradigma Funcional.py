from functools import reduce
lista1 = ['João', 'Maria', 'Carlos']
lista2 = ['da Silva', 'Santos', 'Amorim']

juncao1 = zip(lista1, lista2)
juncao2 = zip(lista1, lista2)
juncao3 = zip(lista1, lista2)

print(list(juncao1))
print(tuple(juncao2))
print(dict(juncao3))


def dobro(x):
    return x*2


def quadrado(x):
    return x**2


def operacao(num, func):
    print(f'O {func.__name__} de {num} é {func(num)}!')


operacao(5, dobro)
operacao(5, quadrado)


def multiplicar(x):
    def calcular(y):
        return x * y
    return calcular


recebe_funcao = multiplicar(5)
recebe_resultado = multiplicar(5)(6)
print(recebe_resultado)
recebe_resultado = recebe_funcao(6)
print(recebe_resultado)

lista = [1, 2, 3, 4]
nova_lista = list(map(lambda i: i * 2, lista))
print(nova_lista, sum(nova_lista))

# nova_lista = map()  # Recebe uma função como parâmetro e devolve uma lista mapeada

# Se for verdadeiro entra na lista se for falso não entra
nova_lista = list(filter(lambda p: p > 1, lista))
print(nova_lista)


valor_inicial = 0
nova_lista = reduce(lambda acumulador, item_atual: acumulador +
                    item_atual, lista, valor_inicial)
print(nova_lista)

#min, max, sum, reversed
lista = list(reversed(lista))
print(lista)
lista = sorted(lista)
print(lista)
print(min(lista))
print(max(lista))
print(sum(lista))

# Generetor
def cores_arco_iris():
    yield 'Vermelho'
    yield 'Laranja'
    yield 'Amarelo'
    yield 'Verde'
    yield 'Azul'
    yield 'Índigo'
    yield 'Violeta'

def incremento_int():
    num = 0
    while True:
        num += 1
        yield num

inc = incremento_int()

for _ in range(10):
    print(next(inc))

def mdc(numeros):
    def calc(divisor):
        return divisor if sum(map(lambda x: x % divisor, numeros)) == 0 \
            else calc(divisor - 1)
    return calc(min(numeros))
