import agenda

print("--------------------", end='\n')
print("   MENU PRINCIPAL")
print("--------------------", end='\n')

arquivo = "Agenda.txt"

opcao = int(input("\n\n1- Criar contato\n2- Listar contatos\n3- Alterar contato\n4- Apagar contato\n5- Sair\n\n"))
while opcao != 5:
    match opcao:
        case 1:
            agenda.le()
            break
        case 2:
            agenda.lista(arquivo)
            break
        case 5:
            print("\nEncerrando programa...\n")
            break

