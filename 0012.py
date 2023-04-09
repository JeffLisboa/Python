# Dicionario
#podemos declarar apenas dentro de chaves {} ou declarando o consultor dict()
#Ex: 1
pessoa = {"nome": "Jefferson", "idade": 33}
#Ex: 2
pessoa = dict(nome="Jefferson", idade="33")

#Podemos tambem acrescentar uma nova chave à um dicionario já existente
#iremos acrescentar o telefone no dicionario pessoa.
pessoa["telefone"] = "31 97112-0374"

#Para acessar aos dados desse dicionario, informamos o nome do dicionario e entre colchetes o nome do dado
pessoa["nome"]
pessoa["telefone"]
pessoa["idade"]
# Ou .get quando nao tiver certeza se a chave existe no dicionario
pessoa.get["nome"]
pessoa.get["telefone"]
pessoa.get["idade"]