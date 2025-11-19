class Motor: 
    def __init__(self, ligado=False):
        self.ligado = ligado

    def ligar_motor(self):
        self.ligado = True

