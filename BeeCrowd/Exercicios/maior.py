# Escreva um programa que leia três números e que imprima o maior
# e o menor.

x = int(input("Numero 1: "))
y = int(input("Numero 2: "))
z = int(input("Numero 3: "))

maior = x
menor = x
if y > maior:
    maior = y
elif x > maior:
    maior = x

if y < menor:
    menor = y
elif x < menor:
    menor = x

print(f"Maior = {maior}\nMenor = {menor}")