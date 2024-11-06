class ContaBancaria():
    def __init__(self, numero_agencia, tipo_conta, saldo, limite, titular):
        self.numero_agencia = numero_agencia
        self.tipo_conta = tipo_conta
        self.saldo = saldo
        self.limite = limite
        self.titular = titular
        self.transacoes = []

    def consultar_saldo(self):
        print(f"\nSaldo Atual: R${self.saldo}")
    
    def saca(self, valor):
        self.transacoes.append(f"Saca:{self.saldo} - {valor}")
        self.saldo -= valor
        self.transacoes.append(f"Saldo:{self.saldo}")


    def deposita(self, valor):
        self.transacoes.append(f"Saca:{self.saldo} + {valor}")
        self.saldo += valor
        self.transacoes.append(f"Saldo:{self.saldo}")
    
    def tansfere_para(self, destino, valor):
        self.transacoes.append(f"Transferencia de {self.titular} para {destino.titular} no valor de R${valor}")
        destino.transacoes.append(f"Transferencia de {self.titular} para {destino.titular} no valor de R${valor}")
        self.saldo -= valor
        destino.saldo += valor
        
        
    