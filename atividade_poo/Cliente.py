class Cliente:
    def __init__(self, nome, sobrenome, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf

    def dados_cliente(self):
        print(f"\nNome: {self.nome} {self.sobrenome}")
        print(f"\nCPF: {self.cpf}")