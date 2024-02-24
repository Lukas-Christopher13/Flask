class Pessoa:
    teste = "lu"

    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

    def falar(self):
        print(self.nome)
        return self.nome
