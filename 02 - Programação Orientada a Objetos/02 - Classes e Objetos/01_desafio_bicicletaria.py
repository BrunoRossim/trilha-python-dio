#declarando a classe para o programa da bicicletaria
class Bicicleta:
    
    def __init__(self, cor, modelo, ano, valor): #inicializando as carateristicas da bicicleta definindo um metodo construtor.
        self.cor = cor#self referencia explixita ao objeto
        self.modelo = modelo#self. igual a atributo da clase
        self.ano = ano
        self.valor = valor

#definindo metodos, são funções dentro de uma classe.
    def buzinar(self):
        print("Plim plim...")

    def parar(self):#para declarar o metodo, def dou nome ao metodo e defino um argumento, neste caso os self.
        print("Parando bicicleta...")
        print("Bicicleta parada!")

    def correr(self):
        print("Vrummmmm...")

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


b1 = Bicicleta("vermelha", "caloi", 2022, 600)
b1.buzinar()
b1.correr()
b1.parar()
print(b1.cor, b1.modelo, b1.ano, b1.valor)#exibindo os atributos da classe

b2 = Bicicleta("verde", "monark", 2000, 189)
print(b2)
b2.correr()
