# Faça um programa que leia duas listas e que gere uma terceira com
# os elementos das duas primeiras

lista1 = list(input().split())
lista2 = list(input().split())
# forma 1 (ruim)

novaLista1 = []
novaLista1.extend(lista1)
novaLista1.extend(lista2)
# forma 2 (decente)

novaLista2 = lista1 + lista2

print(novaLista1)
print(novaLista2)
