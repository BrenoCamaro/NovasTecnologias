import sys

def grava(contato):
    """
    Gravar os argumentos recebidos em um arquivo

    """
    arquivo = open("Agenda.txt", "a")

    for elemento in contato:
        arquivo.write(f"{elemento};")

    arquivo.write("\n")
    arquivo.close()



def le():
    """
    Lê a entrada do usuário e grava em um arquivo

    """
    contato = []

    nome = str(input("\nNome do contato: "))
    telefone = str(input("Telefone: "))
    endereco = str(input("Endereço: "))
    aniversario = str(input("Data de Aniversário: "))

    contato.append(nome)
    contato.append(telefone)
    contato.append(endereco)
    contato.append(aniversario)

    grava(contato)

    




