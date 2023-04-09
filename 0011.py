#Métodos da classe set

#Union
conjunto_a = {1, 2}
conjunto_b = {3, 4}

#Une o conjunto_a e o conjunto_b ficando {1,2,3,4}
conjunto_a.union(conjunto_b)

#Intersection
conjunto_c = {1, 2, 3}
conjunto_d = {2, 3, 4}

#destaca os elementos em comum dos conjuntos ficando {2, 3}
conjunto_c.intersection(conjunto_d)

#Difference
#destaca  os elementos que tem noconjunto_c e nao tem no conjunto_d, ficando {1}
conjunto_c.difference(conjunto_d)
#destaca  os elementos que tem noconjunto_d e nao tem no conjunto_c, ficando {4}
conjunto_d.difference(conjunto_c)

#Symetric_difference
#destaca apenas os elementos em comum dos dois conjuntos. 
#Similar ao difference porem destacando a diferenca dos dois conjuntos ao mesmo tempo.
#ficando assim {1, 4}
conjunto_c.symmetric_difference(conjunto_d)

#Issubset
conjunto_e = {1, 2, 3}
conjunt_f = {4, 1, 2, 5, 6, 3}
#Diz setodos os elementos do conjunto_e estão dentro do conjunto_f
#ficando assim True, pois 1 ,2 e 3 tambem estão dentro do conjunto_f
conjunto_e.issubset(conjunt_f)
#Diz setodos os elementos do conjunto_f estão dentro do conjunto_e
#ficando assim False, pois 4, 5 e 6 não estão dentro do conjunto_e
conjunt_f.issubset(conjunto_e)

#      »»»»»Observações«««««
# .add é utilizado para adicionar valor em um conjunto
# Caso queira acessar os valores de um conjunto é necessário converter para uma lista
# Um conjunto é uma coleção que nao possui objetos repetidos
# .pop, .remove e .del podem ser utilizados para remover elementos de um conjunto