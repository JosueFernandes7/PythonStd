from Testes.Pessoa import Pessoa
from datetime import date
#datas
pessoa1 = Pessoa("Joao", 23)
data = date.today()
data1 = date(2023,2,2)
dataFormatadaUTF = data.strftime("%d/%m/%Y")
print(data.month)
print(dataFormatadaUTF)
print(data1.strftime("%d/%m/%Y"))
pessoa1.apresentar()

#lidando com txt

with open("helloWorld.txt",'r') as arquivo:
    conteudo = arquivo.read()

novoArquivo = open('helloWorld2.txt','w')

novoArquivo.write(conteudo.replace("Lorem Ipsum","TESTE"))
novoArquivo.close()

