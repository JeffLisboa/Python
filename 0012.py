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
print(pessoa["nome"])
print(pessoa["idade"])
print(pessoa["telefone"])

#Para saber se um valor está dentro de um dicionario
#Crie uma variavel onde pergunte se telefone está dentro (in) do dicionario pessoa
consulta = "telefone" in pessoa
#Imprima o resultado
print(consulta)

#Tabem podemos criar dicionarios aninhados
contatos = {
    "contato_1@gmail.com": {"nome": "contato_1", "telefone": "31 99999-1111"},
    "contato_2@gmail.com": {"nome": "contato_2", "telefone": "31 99999-2222"},
    "contato_3@gmail.com": {"nome": "contato_3", "telefone": "31 99999-3333"}
}

# Usar .get quando nao tiver certeza se a chave existe no dicionario
tel= contatos.get("contato_1@gmail.com", {})
print(tel)

