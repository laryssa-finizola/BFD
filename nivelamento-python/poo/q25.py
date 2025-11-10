class Motor: 
    def __init__(self, ligado=False):
        self.ligado = ligado
    
    def ligar_motor(self):
        self.ligado = True

# Objetos
motor1 = Motor()
motor1.ligar_motor()

print(f"Motor está ligado? {motor1.ligado}")