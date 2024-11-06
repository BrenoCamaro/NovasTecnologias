class Historico:
    def __init__(self, data_da_abertura, transacoes):
        self.data_da_abertura = data_da_abertura
        self.transacoes = []
        self.transacoes = transacoes

    def imprime(self):
        for transacao in self.transacoes:
            print(f"\n{self.transacoes}")