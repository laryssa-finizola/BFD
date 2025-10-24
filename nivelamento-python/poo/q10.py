class Lampada:
    def __init__(self):
        self.estado = "Acesa"

    def ligar(self):
        if self.estado  == "Acesa":
            self.estado  = "Apagada"
        else:
            self.estado = "Acesa"

lampada = Lampada()

print(lampada.estado)  

#altera estado
lampada.ligar()
print(lampada.estado) 