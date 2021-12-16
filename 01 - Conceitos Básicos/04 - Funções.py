
#Se vc mudar o valor de arg2 dentro da função ele passa a ser um novo valor padrão
def primeira_funcao(arg1, arg2=.0):
    #arg2 = 1.0 isso faria que o valor padão fosse 1.0 e não 0.0
    return arg1 - arg2 if arg2 != .0 else arg1


print(primeira_funcao(2.0))
print(primeira_funcao(2.0, 3.0))
print(primeira_funcao(arg2=2.0, arg1=3.0))

# Packing empacota tudo em uma tupla


def soma(*nums):
    soma = 0
    for num in nums:
        soma += num
    return soma


print(soma(1, 1))
# Unpacking transforma uma tupla/lista em vários argumentos
print(soma(*(1, 1, 1, 1, 1, 1)))

# *args vira uma tupla
# **kwargs  passa parâmetros nomeados


def resuldados_f1(**podium):
    for posicao, piloto in podium.items():
        print(f'{posicao} -> {piloto}')


resuldados_f1(primeiro='Nome1', segundo='Nome2', terceiro='Nome3')

