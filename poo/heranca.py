#classe mãe: animal
class Animal: 
    def __init__(self, nome, especie):
        self.nome = nome
        self.especie = especie
    
    def comer(self):
        return f"{self.nome} está comendo"
    
#classe filha: cachorro
class Cachorro(Animal):
    def __init__(self, nome, raca):
        super().__init__(nome, especie="Canino")
        self.raca = raca
        
    def latir(self): 
        return f"{self.nome}, da raça {self.raca}, está latindo!"
    
#objeto
meu_cachorro = Cachorro(nome="Rex", raca="Labrador")

#exibição 
print("---HERANÇA---")    
# metódo que foi herdado da classe mãe
print({meu_cachorro.comer()})
# o atributo "especie" tbm foi definido na classe mãe
print(f"espécie: {meu_cachorro.especie}")
#já o metódo latir é exclusivo da subclasse.
print(meu_cachorro.latir())