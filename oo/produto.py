class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
        self.quantidade = 10
    
    def desconto(self, desconto):
        self.preco = self.preco - desconto
        
	#Getter
    @property
    def preco(self):
        return self._preco - 1
    
	#Setter
    @preco.setter
    def preco(self, valor):
        if(isinstance(valor, str)):
            valor = float(valor.replace("R$",""))
            
        self._preco = valor 
    
            
p1 = Produto("Carro", 5000)
#p1.desconto(500)
print(p1.preco)

p2 = Produto("Avião", "R$100000")
p2.desconto(10000)
print(p2.preco)
print(p2.quantidade)

            