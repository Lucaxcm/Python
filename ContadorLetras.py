tex = str(input("Digite Seu Texto --> ")).upper()
tex = sorted(list(tex))
tex.append(1)
v = [0]
for i in range(len(tex)-1):
    b=0
    j=0
    for j in range(0,len(tex)):
        if tex[i] == tex[j]:
            b += 1
        
    if tex[i] not in v:
        print(" / ","'",tex[i],"'","=", b, '\N{SNAKE}', end = " ")
        v.append(tex[i])