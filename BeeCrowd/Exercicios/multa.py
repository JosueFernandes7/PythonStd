# Escreva um programa que pergunte a velocidade do carro de um
# usuário. Caso ultrapasse 80 km/h, exiba uma mensagem dizendo que o usuário
# foi multado. Nesse caso, exiba o valor da multa, cobrando R$ 5 por km acima de
# 80 km/h

velocidade = float(input("Velocidade: "))
multa = 0
if velocidade > 80:
    multa = 5 * int((velocidade - 80))
    print(f"voce foi multado em R$ {multa}, por passar {int((velocidade - 80))}km do limite de 80km/h")
