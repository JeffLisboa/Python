#Fatiamento de string

nome="Jefferson Lisboa Alves da Silva"

#Pega o primeiro caracter da string(lembrando que 0 é o primeiro)
print(nome[0])

#Informa que quer desde o primeiro caracter até o décimo. lembando que 0 é o primeiro
print(nome[:9])

#Informa que quer do décimo primeiro caracter em diante
print(nome[10:])

#Informa que quer do décimo primeiro ao décimo sétimo caracter.
print(nome[10:16])

#Informa que quer do décimo primeiro ao décimo sétimo de 2 em 2
print(nome[10:16:2])

#Pega desde o prieiro caracter da string até o ultimo
print(nome[:])

#pega do primeiro caracter até o ultimo e inverte a ordem
print(nome[::-1])

#Pega o ultimo caracter, se colocar -2 pega os dois ultimos e assim por diante
print(nome[-1])