# resolvido
tamanho = int(input())
for i in range(tamanho):
    finalWord = ""
    strings = input().split()
    word1, word2 = list(strings[0]), list(strings[1])
    maximo = max(len(word1), len(word2))

    for j in range(maximo):
        if j < len(word1):
            finalWord += word1[j]
        if j < len(word2):
            finalWord += word2[j]

    print(finalWord)
