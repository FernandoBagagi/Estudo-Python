class Data(object):
    #o init é o construtor
    def __init__(self, dia, mes, ano):
        self._dia = dia
        self._mes = mes
        self._ano = ano
    def getDia(self):
        return self._dia
    def setDia(self, dia):
        self._dia = dia
    def getMes(self):
        return self._mes
    def setMes(self, mes):
        self._mes = mes
    def getAno(self):
        return self._ano
    def setAno(self,ano):
        self._ano = ano

d = Data(23,2,2020)
print(d.getDia())
print('/')
print(d.getMes())
print('/')
print(d._ano)