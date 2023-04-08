#Desafio básico formação python (Tweet)
#variavel onde sao inseridos os dados do post e lê a quantidade de caracteres
T = (input("Faça um Tweet: "))

#Será verificado se os dados inseridos em T são menores ou igual 140
if len (T) <= 140:
    print("TWEET")

else:
    print("MUTE") 

  