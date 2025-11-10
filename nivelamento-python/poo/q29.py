class Computador:
    def __init__(self, estado):
        self.estado = estado
    
    def info(self):
        if self.estado == True:
            return "computador ligado"
        else:
            return "computador desligado"

teste1 = Computador(True)
print(teste1.info())

teste2 = Computador(False)
print(teste2.info())