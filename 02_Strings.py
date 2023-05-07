texto = "João e Maria comem pão"

# iterar sobre strings

for i in texto:
    print(i,end=" ") # caracter por caracter

# tamanho da string
print(len(texto))

# Operacoes com strings

# Concatenação
s = "ABC"
print(s*4 + "Teste")

# Composição
idade = 22
print("[%d]" % idade)
print("[%3d]" % idade)
print("[%03d]" % idade)
print("[%-3d]" % idade)
salario = 5200.234
nome = "Pedro"
print("%s tem %d anos e recebe R$ %.2f" % (nome, idade, salario))

# Fatiamento
s = "ABCDEFGHI"
print(s[0:2]) # ou s[:2], pode-se omitir o primeiro termo
print(s[:-2]) # tira os dois ultimostr