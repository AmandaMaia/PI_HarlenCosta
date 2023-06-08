import random
jogador1 = random.randint(1,3)
jogador2 = int(input())

msg = "Digite 0 (pedra), 1 (papel) ou 2 (tesoura)"


if jogador1 == 1 and jogador2 == 0:
    #pedra, papel
        status1=True #jogador 1 ganhou
        status2=False #jogador 2 perdeu
elif jogador1 == 0 and jogador2 == 1:
        status1=False 
        status2=True 
elif jogador1 == 1 and jogador2 == 2:
    #papel,tesoura
        status1=False 
        status2=True 
elif jogador1 == 2 and jogador2 == 1:
        status1=False 
        status2=True 
elif jogador1 == 2 and jogador2 == 0:
    #tesoura,pedra
        status1=False 
        status2=True 
elif jogador1 == 0 and jogador2 == 2:
        status1=False 
        status2=True
elif jogador1 == jogador2:
      status1=True 
      status2=True
else:
      status1=False
      status2=False

if status1 == True and status2 == False:
    mensagem1 = "O jogador 1 venceu!"
    mensagem2 = "O jogador 2 perdeu"
elif status1 == False and status2 == True:
    mensagem1 = "O jogador 1 perdeu"
    mensagem2 = "O jogador 2 venceu!"    
elif status1 == True and status2 == True:
    mensagem = "empate"
else:
    mensagem = "resultado invalido"

print(jogador1)
print(jogador2)
print(mensagem)
