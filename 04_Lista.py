# # lista vazia

# L = []

# #  Uma lista com três elemento

# Z = [15, 8, 9]

# # Acesso a um item

# print(Z[0])

# #  Modificação de uma lista
# Z[1] = 20
# print(Z)

# # Media

# notas = [6,7,5,9,8]
# soma = 0
# x = 0

# for nota in notas:
#     soma += nota

# media = soma / len(notas)
# # forma antiga = print("Média: {:.2f}".format(media))
# print(f"Média: {media:.2f}")

# # Copiar Listas em Python

# # Forma Errada!!!!
# L=[1,2,3,4,5]
# V=L

# V[0] = 3000
# print(L,V) # [3000, 2, 3, 4, 5] [3000, 2, 3, 4, 5]
# # dessa forma eu estou pegando a referencia de l e não copiando em si e criando uma nova lista

# # Forma Correta
# T=[1,2,3,4,5]
# J= T[:]

# J[0] = 3000
# print(J,T) # [3000, 2, 3, 4, 5] [1, 2, 3, 4, 5]
# # dessa forma altera somente a lista J

# # o simbolo [:] representa tudo, porem pode-se pegar parter
# # [0:2] ou [:2] pega os 2 primeiros elementos
# # [-2] vai pegar todos menos os 2 ultimos

# L = T[:-2]
# print(L) # 1,2,3

# # adicionar item

# lista = [5,10,2,-3]
# lista.append(4) # [5,10,2,-3,4]
# print(lista)

# # adicao de listas

# l = [20]
# j = [1,4,9,12,23]
# k = l + j
# print(k) # [20, 1, 4, 9, 12, 23]
# print(j + l )# [1, 4, 9, 12, 23, 20]

# # Adição de elementos e listas
# L = ["a"]
# L.append("b")
# # L = ["a","b"]
# print(L)

# # com listas se usa o extend, ou o +=

# L.extend(["c","d"])
# print(L)

# # Remocao de elementos da lista

# # – Remoção de elementos
# L = ["a","b","c"]
# del L[1] # remove b
# print(L)

# # – Remoção de fatias

# L = list(range(101))
# del L[1:99]
# print(L) # [0,99,100]

# lista = list(range(128))
# print(lista["A"])
# #iterar lista

# mapa = {"nome":"josue","idade":20}

# print(mapa)
# x = 2

# y = [x] * 10 # faz com que faça um array com x 10 vezes [2,2,2,2,2,2,2,2]
# print(y)
# # print(lista[3])

# enumerate
# lista = [1,2,3,223,21,2,55]
# print("[",end="")
# for i,elemento in enumerate(lista):
#     if i != len(lista) - 1:
#         print(i,end=", ")
#     else:
#         print(i,end="")
        

# print("]",end="")

# Exercício 6.13 A lista de temperaturas de Mons, na Bélgica, foi armazenada na lista 
# T = [ -10, -8, 0, 1, 2, 5, -2, -4]. Faça um programa que imprima a menor e a maior 
# temperatura, assim como a temperatura média.

# # Solução
# T = [ -10, -8, 0, 1, 2, 5, -2, -4]
# maior, menor, media = T[0],T[1],0
# for temperature in T:
#     media += temperature
#     if temperature > maior:
#         maior = temperature
#     if temperature < menor:
#         menor = temperature
# media = media / len(T)
# print(T)
# print(f"Media = {media}")
# print(f"Maior = {maior}")
# print(f"Menor = {menor}")