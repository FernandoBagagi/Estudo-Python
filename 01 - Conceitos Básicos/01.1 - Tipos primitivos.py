"""
Uma variável em Python tem valores dinamicos, ou seja, ela pode ser, em um dado momento,
inteira e ao receber uma string passar a ser do tipo string. Para verificar se uma variável
é se dum determinado tipo usamos a função type() que retorna qual tipo aquela variável é.
Lembrando que Python é considerada uma linguagem fortemente tipada pois os tipos primitivos
existem e uma variável é do tipo do valor que ela recebe. Em outros termos, ao inicializar
uma variável ela recebe um tipo e permaneece com esse tipo até receber um outro valor de
outro tipo.
"""
variável = 1
print(type(variável))
variável = 5.2
print(type(variável))
variável = 'Palavra'
print(type(variável))
