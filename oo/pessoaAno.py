from random import randint

class PessoaAno:
    ano = 2023
    
    def __init__(self, dataDeNacimento):
        self.dataDeNacimento = dataDeNacimento
    
    def getIdade(self):
        print(self.ano - self.dataDeNacimento)

    @classmethod
    def getAno(cls):
        return cls.ano
    
    @staticmethod
    def getRandom(): 
        return 12
    
    
    
        
            
        
		