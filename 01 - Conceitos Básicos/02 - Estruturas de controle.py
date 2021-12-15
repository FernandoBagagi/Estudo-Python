nota = .5
# Permite intervalos
if 7.0 <= nota <= 10.:
    print('Aprovado')
# elif nota in range(4.0, 7.0, 0.01):
elif nota >= 4.:
    print('Recuperação')
else:
    print('Reprovado')

while nota < 10.0:
    print(nota)
    nota += 0.1

print(nota)

lista = ["Nome1", "Nome2", "Nome3", "Nome4", "Nome5"]

for indice, nome in enumerate(lista):
    print(f"{indice} - {nome}")

# depois de sair do for

print(indice, nome)

# break, continue

for i in range(0, 10):
    print("Entra aqui")
else:
    print('Entra aqui quando sai')

while i < 20:
    i += 1
else:
    print("Entra aqui quando sai do while")
