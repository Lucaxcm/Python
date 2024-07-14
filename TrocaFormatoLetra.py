LETRA = str(input("Digite Uma Letra: "))
COD = ord(LETRA)
CONTRARIO = (LETRA.casefold())
COD2 = ord(CONTRARIO)
    
if COD == COD2:
    print(LETRA.upper())       
else:
    print(LETRA.casefold())