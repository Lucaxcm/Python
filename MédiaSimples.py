num = 1
num2 = 0
ado = 0

while True:
    if num == 0:
        break
    
    else:
        num = int(input("Digite um Valor (Zero Para Parar): "))
        num2 = num2 + num
        ado = ado + 1
        
ado = ado - 1
print(f"\nA Média é: {num2/ado:.2f}")
print("Quantidade de Números Digitado:", ado)
print("Soma dos Números Digitados:", num2)