#Stings de multiplas linhas ou strings triplas

nome = "Jefferson"
#Colocando a formatação diretamente na variavel e respeitando o espaçamento que foi dado na frase
mensagem = f""""
    Olá, me nome é {nome}!
"""
print(mensagem) 

#Com as 3 aspas, ele respeita todo espaçamento que coloquei sem ter que formatar
print(
    """"
    ======== MENU ========

    1 - Consultar saldo
    2 - Depositar
    3 - Sacar
    4 - Sair
    ======================
"""    
)


texto = " Python".lstrip()
print(texto)