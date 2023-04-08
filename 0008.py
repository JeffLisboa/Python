#Metodos da classe lista

#Lista vazia que será preenchida com o que for informado no .append
churrasco = []

#.append, tudo que for informado aqui será preenchido na lista linguagem que está vazia
churrasco.append("Carvão, Contra filé, Fraldinha, Toucinho de barriga, Linguiça")
print(churrasco)

#.pop remove o ultimo item da lista, mas tambem posso dar a coordenada de qual item quero que ele remova
churrasco = ["Carvão", "Contra filé", "Fraldinha", "Toucinho de barriga", "Linguiça"]

#Remove o iltimo item da lista
churrasco.pop()
print(churrasco)


churras = ["Carvão", "Contra filé", "Fraldinha", "Toucinho de barriga", "Linguiça"]

#Remove o item escolhido(0 based)
churras.pop(1)
print(churras)

#sorted ordena por ordem alfabetica
print(sorted(churras))

