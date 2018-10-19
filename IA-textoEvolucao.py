import string
import random
import time

characteresPossiveis = string.ascii_lowercase + string.digits + string.ascii_uppercase + ' .,!?;:'

alvo = input("Insira sua palavra alvo: ")
tentarEste = ''.join(random.choice(characteresPossiveis) for i in range(len(alvo)))
tentarProx = ''

completo = False

geracao = 0

while completo == False:
    print(tentarEste)
    tentarProx = ''
    completo = True
    for i in range(len(alvo)):
        if tentarEste[i] != alvo[i]:
            completo = False
            tentarProx += random.choice(characteresPossiveis)
        else:
            tentarProx += alvo[i]
    geracao += 1
    tentarEste = tentarProx
    time.sleep(0.1)

print("Alvo atingido! Isto levou " + str(geracao) + " geracoes(ao)")
