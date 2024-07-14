import random
num = random.randrange(1,101)
palpite = int(input("Digite Seu Palpite: "))
tentativas = 1
    
while True:
        
    if palpite == num:
        break
        
    elif palpite < num:
        print("Valor Abaixo")
        palpite = int(input("Tente Novamente: "))
        tentativas +=1
        
    elif palpite > num:
        print("Valor Alto")
        palpite = int(input("Tente Novamente: "))
        tentativas +=1
        
print("\nAcertou Com", tentativas, "Tentativas")