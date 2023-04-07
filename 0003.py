nome = str(input("Digite seu nome: "))
idade = int(input("Digite sua idade: "))
profissao = str(input("Diga sua profissão : "))

#Usando Format(f) no inicio da string. OBS: .title e .captalize tem o mesmo efeito (Deixar a primeira letra maiuscula)
print(f"Meu nome é {nome.title()}, tenho {idade} anos e eu sou {profissao.capitalize()}!\n")
 
#Forma diferente criando uma lista(dados) e destacando a baixo
#Obs, utilizei as variaveis em ingles para diferenciar do exemplo a cima
dados ={"name": "jefferson", "age": 33}
print("Meu nome é {name}, tenho {age} anos!".format(**dados))