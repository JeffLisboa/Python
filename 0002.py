# Manipulação de texto (strings)

nome = "JeFfErSoN"

#Converte tudo para MAIUSCULO
print (nome.upper()) 

#Converte tudo para minusculo
print (nome.lower()) 

#Converte a primeira letra para Maiusculo
print (nome.title()) 

texto = "  Olá Mundo !  "
print (texto)

#Tira o espaçamento da direita e esquerda
print (texto.strip())

#Tira o espaçamento da direita 
print (texto.rstrip()) 

#Tira o espaçamento da esquerda
print (texto.lstrip()) 

curso = "Python"

#Alinha ao centro preenchendo o inicio e o fim com espaço em branco até somar 10 
# contando com as letras da palavra
print (curso.center(10)) 

#Alinha ao centro e preenche o inicio e o fim da palavra 
#com o simbolo informado(#) até completar 10 caracteres
print (curso.center(10, "#")) 

#Coloca o caracter informado (.) entre cada letra da palava
print (".".join(curso))


#Testando tambem com laço de repetição
for letra in curso:
    print (letra, end= "-")
   
