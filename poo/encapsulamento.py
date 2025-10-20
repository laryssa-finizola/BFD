class ContaBancaria:
    def __init__(self, saldo_inicial):
        self.__saldo = saldo_inicial
        
    #get
    def consultarSaldo(self):
        return f"saldo atual = R${self.__saldo:.2f}"
    
    #setter
    def depositar(self, valor):
        if valor>0:
            self.__saldo += valor
            return f"depósito de R${valor:.2f} realizado."
        else:
            return "valor de depósito inválido."
        
#criação do objeto
minha_conta = ContaBancaria(saldo_inicial=500)

#exibição
print("------ENCAPSULAMENTO------")
print(minha_conta.consultarSaldo())
print(minha_conta.depositar(150))
#ao tentar alterar o saldo diretamente, o encapsulamento gera erro
## minha_conta.__saldo = 1000000
print(minha_conta.consultarSaldo())