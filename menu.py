import agenda

print("--------------------", end='\n')
print("   MENU PRINCIPAL")
print("--------------------", end='\n')

arquivo = "Agenda.txt" # Nome do arquivo/agenda
rodando = True

while rodando:
    opcao = int(input("\n\n1- Criar contato\n2- Listar contatos\n3- Alterar contato\n4- Apagar contato\n5- Sair\n\n"))
    match opcao:
        case 1:
            agenda.le()
        case 2:
            agenda.lista(arquivo)
        case 5:
            print("\nEncerrando programa...\n")
            rodando = False
        case _:
            print("\nOpção Inválida!\n")

