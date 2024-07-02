# Funções de cálculo

def Mult(n1, n2):   # Multiplicação
    return n1 * n2

def Div(n1, n2):    # Divisão
    if n2 == 0:
        raise ValueError("Divisão por zero não é permitida!")
    return n1 / n2

def Reci(n1):       # Recíproco
    if n1 == 0:
        raise ValueError("Não é possível calcular o recíproco de zero!")
    return 1 / n1

def Po(n1, n2):     # Potência
    return n1 ** n2

def Fa(n1):         # Fatorial
    if n1 == 0:
        return 1
    else:
        v = int(n1)
        for i in range(v - 1, 1, -1):
            v *= i
        return v

def Cient(resposta): # Resposta em Notação Científica
    if resposta > 0:
        return f"{resposta:.2e}"
    else:
        return f"{resposta:.2e}"

# Loop principal do programa
while True:
    print("Qual cálculo deseja realizar:\n")
    print("Soma..............[+]")
    print("Subtração.........[-]")
    print("Multiplicação.....[*]")
    print("Divisão...........[/]")
    print("Recíproco.........[~]")
    print("Potência..........[^]")
    print("Fatorial..........[!]")
    print("Sair...........[SAIR]")

    escolha = input("\nQual operação deseja? ").strip()

    if escolha == 'SAIR':
        break
    elif escolha in ['+', '-', '*', '/', '~', '^', '!']:
        # Executar cálculos baseados na escolha do usuário
        if escolha == "+":
            n1 = float(input("\nPrimeiro valor: "))
            n2 = float(input("\nSegundo valor: "))
            resposta = n1 + n2

        elif escolha == "-":
            n1 = float(input("\nPrimeiro valor: "))
            n2 = float(input("\nSegundo valor: "))
            resposta = n1 - n2

        elif escolha == "*":
            n1 = float(input("\nPrimeiro valor: "))
            n2 = float(input("\nSegundo valor: "))
            resposta = Mult(n1, n2)

        elif escolha == "/":
            n1 = float(input("\nPrimeiro valor: "))
            while True:
                n2 = float(input("\nSegundo valor: "))
                try:
                    resposta = Div(n1, n2)
                    break
                except ValueError as e:
                    print(e)

        elif escolha == "~":
            n1 = float(input("\nValor: "))
            resposta = Reci(n1)

        elif escolha == "^":
            n1 = float(input("\nBase: "))
            n2 = float(input("\nExpoente: "))
            resposta = Po(n1, n2)

        elif escolha == "!":
            n1 = int(input("\nValor: "))
            resposta = Fa(n1)

        # Imprimir o resultado em notação regular e científica
        print(f"\nA resposta é {resposta}")
        rescie = Cient(resposta)
        print(f"A resposta em notação científica é {rescie}\n")
    else:
        print("\nOperação incorreta!\n")

print("\nObrigado por utilizar a calculadora!")
