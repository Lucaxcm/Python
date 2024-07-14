Ado1 = 0
Ado2 = 1  
Nota = -1

while Ado1 <= Ado2:

        while Nota < 0:
            Nota = int(input("Digite a Tabuada que deseja: "))
            Ado1 = int(input("Digite o Inicio: "))
            Ado2 = int(input("Digite a Final: "))
    
        print(Nota,"x", Ado1, " =",Nota*Ado1)
        Ado1 = Ado1 + 1