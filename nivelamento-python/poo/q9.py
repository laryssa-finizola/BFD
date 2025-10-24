class Computador:
    def __init__(self):
        self.ligado = False

    def ligar(self):
        if self.ligado  == False:
            self.ligado  = True
        else:
            self.ligado = False

computador = Computador()

print(computador.ligado)  

#teste: 
computador.ligar()
print(computador.ligado)