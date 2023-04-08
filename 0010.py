#Entrada com o numero do mês
month = int(input("Escreva o numero do mês desejado: "))

#Números de 1 à 12 atribuídos aos seus respectivos meses por extenso
months_dict = {1 : "January", 2: "February", 3: "March", 4:"April", 5: "May", 6:"June", 7:"July", 8:"August", 9: "Semptember", 10: "October", 11: "November", 12:"December"}

#condicional para numeros de 1 à 13(para no 12) armazena a na variavel x a outra variavel months_dict com .get 
# para pegar o valor inserido na entrada e depois printar a variavel x
if month in range (1,13):
    x = months_dict.get(month)
    print(x)

#Tambem funciona da forma a baixo
month = input("Escreva o numero do mês desejado: ")

months_dict = {
"1":"January", "2":"February", "3":"March", "4":"April", "5":"May", "6":"June", "7":"July", "8":"August", "9":"September", "10":"October", "11":"November", "12":"December"
}
if month== "1":
 print(f"{months_dict['1']}")
if month=="2":
    print(f"{months_dict['2']}")
if month=="3":
    print(f"{months_dict['3']}")
if month=="4":
    print(f"{months_dict['4']}")
if month=="5":
    print(f"{months_dict['5']}")
if month=="6":
    print(f"{months_dict['6']}")
if month=="7":
    print(f"{months_dict['7']}")
if month=="8":
    print(f"{months_dict['8']}")
if month=="9":
    print(f"{months_dict['9']}")
if month=="10":
    print(f"{months_dict['10']}")
if month=="11":
    print(f"{months_dict['11']}")
if month=="12":
    print(f"{months_dict['12']}")
