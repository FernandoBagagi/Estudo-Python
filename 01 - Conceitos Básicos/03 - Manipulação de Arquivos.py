arquivo = open("01 - Conceitos Básicos/teste.txt", encoding='utf-8')
conteudo = arquivo.read()
arquivo.close()

for linhas in conteudo.splitlines():
    print("{0} possui {1} anos, {2}m de altura e eEstudante {3}".format(
        *linhas.split(",")))





