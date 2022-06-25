"""arquivo = open('teste.txt', 'w+')
arquivo.write('Esse é um teste\npara ver\nse tude\nestá indo\nbem\n')
arquivo.close()

ler = open('teste.txt', 'r')
aux = ler.read()
#aux = "Lendo o arquivo"
#while aux != None:
    #aux = ler.readline()
print (aux)
ler.close()

acrescentar = open('teste.txt', 'a')
acrescentar.write('Adicionar no final')
acrescentar.close()
"""
ler2 = open('teste.txt', 'r')
aux2 = ler2.readline()
while aux2 != "":
    print(aux2)
    aux2 = ler2.readline()
ler2.close()