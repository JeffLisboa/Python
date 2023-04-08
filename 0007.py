#Listas e tuplas.
#OBS: os dados de uma lista os dados sao do mesmo tipo, já na tupla os dados podem ser de tipos distintos como string, int e float juntos

#Lista utilizando o construtir list
churrasco = list(["Carvão", "Contra filé", "Fraldinha", "Toucinho de barriga", "Linguiça"])
print(churrasco)


#Cria uma lista com as strings informadas
frutas = (
    "laranja",
    "pera",
    "uva",
)
print(frutas)

#Lista usando apenas colchetes sem ter que informar o construtor list
convidados = ["joão", "Maria", "Dalva", "Bento"]
print(convidados)
#Tambem é possível fatiar uma lista(0 based)
print (convidados[0])
print (convidados[3])
print (convidados[:3])
print (convidados[2:])
print (convidados[::-1])


#A estrutura tuple vai separar todas as letras da string informada
letras = tuple("python")
print(letras)

#Cria uma lista de numeros inteiros separados com as vírgulas já informadas sem acrescentar mais virgula na execução do código
numeros = tuple([1, 2, 3, 4])
print(numeros)

pais = ("Brasil",)
print(pais)