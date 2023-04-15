#Função é um trecho de código que realiza uma tarefa específica e pode ser chamado em diferentes partes de um programa, sem 
#a necessidade de reescrever o código toda vez que a tarefa precisa ser realizada.

def exibir_mensagem():
    print("Olá mundo!")

def exibir_mensagem_2(nome):
    print(f"Seja bem vindo, {nome}!")

def exibir_mensagem_3(nome="Anônimo"):
    print(f"Seja bem vindo {nome}!")  



#Para exibir ou executar o que foi definido na função, é necessário chamar a função pelo identificador dela
# e se necessário dentro dos parênteses informar um argumento, exemplo:

#A função exibir_mensagem não recebe nenhum argumento e simplesmente imprime a mensagem "Olá mundo!"
exibir_mensagem()

 
#A função exibir_mensagem_2 recebe um argumento nome e imprime uma mensagem de boas vindas com esse nome.
exibir_mensagem_2(nome="Jeff")    


#A função exibir_mensagem_3 também recebe um argumento nome, mas caso esse argumento não seja passado, ela utiliza um valor padrão "Anônimo". 
exibir_mensagem_3(nome="Jefferson")
exibir_mensagem_3()


#Também existe funções com argumentos nomeados como por exemplo:

def salvar_carro(marca, modelo, ano, placa):
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")

salvar_carro("Fiat", "Idea", 2011, "KVX-E245")
#Ou podemos inverter a ordem desde que especifiquemos o nome do parametro
salvar_carro(placa="KVX-E245", modelo="Idea", ano=2011, marca="Fiat")