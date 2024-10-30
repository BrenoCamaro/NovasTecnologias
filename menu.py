import agenda

print("--------------------", end='\n')
print("   MENU PRINCIPAL")
print("--------------------", end='\n')

opcao = int(input("1- Criar contato\n2- Listar contatos\n3- Alterar contato\n4- Apagar contato\n\n"))
match opcao:
    case 1:
        agenda.le()

