nome = str(input("Digite seu nome: "))
idade = int(input("Digite sua idade: "))
genero = str(input("Diga se é do gênero Masculino ou Feminino: "))

if nome and genero != str or idade!= int:
 print("Digite apenas letras no Nome e no Gênero e apenas números na Idade!")
 nome = str(input("Digite seu nome: "))
 idade = int(input("Digite sua idade: "))
 genero = str(input("Diga se é do gênero Masculino ou Feminino: "))
 print (f"Olá! Me chamo {nome}, tenho {idade} anos, do gênero {genero.title()}.") 
    
  
else:
  print (f"Olá! Me chamo {nome}, tenho {idade} anos, do gênero {genero.title()}.") 



