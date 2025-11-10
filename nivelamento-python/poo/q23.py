class Pessoa: 
    def __init__(self, idade):
        self.idade = idade

    def maior_idade(self):
        if self.idade >= 18:
            return True
        else:
            return False
        
p1 = Pessoa(20)
print(f"Pessoa 1 tem maior idade? : {p1.maior_idade()}")

p2 = Pessoa(15)
print(f"Pessoa 2 tem maior idade? : {p2.maior_idade()}")