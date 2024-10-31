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

    return contato


def lista(nomeArquivo):
    """
    Faz a leitura do arquivo cujo nome for passado como argumento
    """
    arquivo = open(f"{nomeArquivo}", "r")
    linha = arquivo.readline()

    while linha != "":
        print(linha)
        linha = arquivo.readline()

    arquivo.close()

def apaga(nomeArquivo, numeroDaLinha):
    """
    Apaga um registro do arquivo informado como arqumento na linha passada como argumento
    """
    arquivo = open(f"{nomeArquivo}", "r")
    linhas = arquivo.readlines()

    if 0 <= numeroDaLinha < len(linhas):
        del linhas[numeroDaLinha]
    else:
        print("\nNúmero da linha inválido!\n")

    arquivo.close()

    arquivo = open(f"{nomeArquivo}", "w")
    arquivo.writelines(linhas)
    arquivo.close()


def contarLinhas(nomeArquivo):
    """
    Retorna a quantidade de linhas do arquivo recebido como argumento
    """
    arquivo = open(f"{nomeArquivo}", "r")
    linhas = arquivo.readlines()
    arquivo.close()
    return len(linhas)


