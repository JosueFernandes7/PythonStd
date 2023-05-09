# FORMA 1
lista1 = list(input().split())
lista2 = list(input().split())
lista3 = []
print(lista1)
print(lista2)
for elemento in lista1:
    if elemento not in lista3:
        lista3.append(elemento)

for elemento in lista2:
    if elemento not in lista3:
        lista3.append(elemento)

print(lista3)

# FORMA 2

lista4 = []

for elemento in lista1:
    if not lista4.__contains__(elemento):
        lista4.append(elemento)

for elemento in lista2:
    if not lista4.__contains__(elemento):
        lista4.append(elemento)
print(lista4)