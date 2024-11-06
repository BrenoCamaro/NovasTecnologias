import ContaBancaria
import Historico
import Cliente

cliente1 = Cliente.Cliente("Breno", "Camarô", "000.000.000-00")
cliente1.dados_cliente()

conta_cliente1 = ContaBancaria.ContaBancaria(1, "Corrente", 1000, 0, cliente1.nome)

cliente2 = Cliente.Cliente("Meire", "Sousa", "111.100.100-00")
cliente2.dados_cliente()

conta_cliente2 = ContaBancaria.ContaBancaria(2, "Corrente", 3000, 0, cliente2.nome)
conta_cliente2.consultar_saldo()
conta_cliente1.consultar_saldo()
conta_cliente2.tansfere_para(conta_cliente1, 1000)

print(f"\nHistórico de {cliente2.nome}")
cliente2_historico = Historico.Historico("06/11/24", conta_cliente2.transacoes)
cliente2_historico.imprime()
conta_cliente2.consultar_saldo()

print(f"\nHistórico de {cliente1.nome}")
cliente2_historico = Historico.Historico("06/11/24", conta_cliente1.transacoes)
cliente2_historico.imprime()
conta_cliente1.consultar_saldo()



