import ContaBancaria

c1 = ContaBancaria.ContaBancaria(1, "Salário", 1000, 0)
c2 = ContaBancaria.ContaBancaria(2, "Salário", 1000, 0)

c1.tansfere_para(c2, 500)
c1.consultar_saldo()
c2.consultar_saldo()
