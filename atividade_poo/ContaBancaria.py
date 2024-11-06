class ContaBancaria():
    def __init__(self, numero_agencia, tipo_conta, saldo, limite):
        self.numero_agencia = numero_agencia
        self.tipo_conta = tipo_conta
        self.saldo = saldo
        self.limite = limite

    def consultar_saldo(self):
        print(f"\nSaldo Atual: R${self.saldo}")
    
    def saca(self, valor):
        self.saldo -= valor

    def deposita(self, valor):
        self.saldo += valor
    
    def tansfere_para(self, destino, valor):
        destino.deposita(valor)
        self.saca(valor)
        
    