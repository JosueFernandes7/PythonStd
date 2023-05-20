# Sr. Amnésio tinha uma grande dificuldade em guardar senhas. Para lembrá-las, ele sempre usava números, e as escrevia em pedaços de papel,
# que também perdia com facilidade, fazendo com que ele precisasse modificar a senha cada vez que isto acontecia.
# Cansado, ele pensou em uma forma mais prática: colocava no papel um número próximo da senha, depois ele usava sempre uma mesma conta para lembrar a senha,
# baseada no número escrito no papel. Mas ele também esquecia a fórmula, por isto, pediu para você escrever um programa que, dado o número do papel, informe a senha correspondente.
#
# Escreva um programa que, dado um número, informe a respectiva senha.

while True:
    entrada = input().split()
    numero = int(entrada[0])
    print(numero - 1)