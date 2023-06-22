import somasub # <-- Importando o módulo somasub

salario = 5000
bonus = 2000
despesas = 4000

receita = somasub.soma(salario, bonus)        # <- Prefixo somasub
saldo = somasub.subtracao(receita, despesas)  # <- Prefixo somasub

print("O saldo é: ", saldo)