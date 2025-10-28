class Celular:
    def __init__(self, bateria):
        self.bateria = bateria

    def carregar(self): 
        if self.bateria < 100:
            self.bateria += 10
        else:
            print("Bateria cheia!")

celular = Celular(50)
print(f"Estado da bateria: {celular.bateria}%")
celular.carregar()
print(f"Estado da bateria: {celular.bateria}%")
celular.carregar()
print(f"Estado da bateria: {celular.bateria}%")