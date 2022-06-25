
class Pessoa:
    
    def __init__(self, nome, idade = None):
        self.nome = nome
        self.idade = idade
    
    def __str__(self):
        apresentacao = "Meu nome é " + self.nome
        if self.idade:
            apresentacao += " e tenho " + self.idade.__str__() + " anos"
        return apresentacao

    def isAdult(self):
        if self.idade:
            return self.idade >= 18
        return False


class Vendedor(Pessoa):

    def __init__(self, nome, idade, salario):
        super().__init__(nome, idade)
        self.salario = salario

class Compra:

    def __init__(self, vendedor, data, valor):
        self.vendedor = vendedor
        self.data = data
        self.valor = valor

class Cliente(Pessoa):

    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self.compras = []

    def resgistrarCompra(self, compra):
        self.compras.append(compra)

    def getTotal(self):
        total = 0.0
        for aux in self.compras:
            total += aux.valor
        return total

    def getDataUltimaCompra(self):
        #Verificar se está correto
        if len(self.compras) > 0:
            datas = []
            for aux in self.compras:
                datas.append(aux.data)
            sorted(datas)
            return datas[- 1]
        else:
            print("Não foi possível encontrar a data da última compra!")
            return -1

pessoas = [Pessoa(nome = "João", idade = 18),Pessoa(nome = "Maria")]
for aux in pessoas:
    print(aux)