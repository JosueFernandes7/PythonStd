# lista vazia

L = []

#  Uma lista com três elemento

Z = [15, 8, 9]

# Acesso a um item

print(Z[0])

#  Modificação de uma lista
Z[1] = 20
print(Z)

# Media

notas = [6,7,5,9,8]
soma = 0
x = 0

for nota in notas:
    soma += nota

media = soma / len(notas)
# forma antiga = print("Média: {:.2f}".format(media))
print(f"Média: {media:.2f}")

# Copiar Listas em Python

# Forma Errada!!!!
L=[1,2,3,4,5]
V=L

V[0] = 3000
print(L,V) # [3000, 2, 3, 4, 5] [3000, 2, 3, 4, 5]
# dessa forma eu estou pegando a referencia de l e não copiando em si e criando uma nova lista

# Forma Correta
T=[1,2,3,4,5]
J= T[:]

J[0] = 3000
print(J,T) # [3000, 2, 3, 4, 5] [1, 2, 3, 4, 5]
# dessa forma altera somente a lista J

# o simbolo [:] representa tudo, porem pode-se pegar parter
# [0:2] ou [:2] pega os 2 primeiros elementos
# [-2] vai pegar todos menos os 2 ultimos

L = T[:-2]
print(L) # 1,2,3