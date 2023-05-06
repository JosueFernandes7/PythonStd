
def verificaDiscagem(ddd):
    for chave,valor in discagem.items():
        if (ddd == chave):
            return print(valor)

    return print("DDD nao cadastrado")

discagem = {}
discagem[61] = "Brasilia"
discagem[71] = "Salvador"
discagem[11] = "Sao Paulo"
discagem[21] = "Rio de Janeiro"
discagem[32] = "Juiz de Fora"
discagem[19] = "Campinas"
discagem[27] = "Vitoria"
discagem[31] = "Belo Horizonte"
ddd = int(input())

verificaDiscagem(ddd)
