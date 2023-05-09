
while True:
    entrada = input().split()
    a = int(entrada[0])
    if a == 0:
        break
    b = int(entrada[1])
    if b == 0:
        break
    c = int(entrada[2])
    if c == 0:
        break
    tamanhoTerreno = a * b * 100 / c
    lado = 1
    while True:
        if lado * lado > tamanhoTerreno:
            lado -= 1
            break
        elif lado * lado == tamanhoTerreno:
            break
        else:
            lado += 1
    print(lado)