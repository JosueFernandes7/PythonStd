# entrada de dados
"""
# por default o input é sempre str
entrada = input()

print(type(entrada)) # class str
#conversoes
numero1 = int(input())
numero2 = float(input())
print(f"soma = {int(numero1 + numero2)}")
"""

# Faça um programa que peça dois números inteiros. Imprima a soma
# desses dois números na tela.
numero1 = int(input())
numero2 = int(input())
soma = numero1 + numero2
print(soma)

# Escreva um programa que leia um valor em metros e o exiba convertido em milímetros
valor = float(input("Valor em metros: "))
valorEmMilimetros = valor * 1000
print("\nValor em milímetros = %.2f" % valorEmMilimetros)

# uma outra forma

entrada = input().split()