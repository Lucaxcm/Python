def pontos(horatual):
    
    while True:
        
        horatual2 = (list(horatual))
        
        if horatual2[2] != ":":
            
            print("Modo de Digitação invalida digite novamente!\n")
            horatual = input("Que horas são?1\n--> ")
            
        else:
            return horatual
        
def valores(horatual):
    
    
    while True:
        
        horatual2 = int(horatual[0])
        horatual3 = int(horatual[1])
        
        if ((horatual2 < 0) or (horatual2 > 24)) or ((horatual3 < 0) or (horatual3 >= 60)):
            print("Horas invalidas digite novamente!2")
            horatual = (input("\n--> "))
            horatual = pontos(horatual)
            horatual = ((horatual).split(":"))
            horatual2 = int(horatual[0])
            horatual3 = int(horatual[1])
        else:
            horatualverdadeira = horatual
            return horatualverdadeira
         
while True:
    try:
        horatual = input("Que horas são?\n--> ")
        horatual = pontos(horatual)
    except(IndexError):
        print("valor invalido")
        horatual = input("Que horas são?\n--> ")
    else:
        break

horatual = (horatual).split(":")
horatualverdadeira = valores(horatual)
v1= int(horatualverdadeira[0])
v2= int(horatualverdadeira[1])


if ((v1 == 12) and (v2 > 0)):
    print(horatualverdadeira[0],":",horatualverdadeira[1]," PM")
    
elif (v1 > 12):
    v1 = v1-12
    print(v1,":",horatualverdadeira[1], "PM")

elif (v1 < 12):
    print(horatualverdadeira[0],":",horatualverdadeira[1], "AM")




    