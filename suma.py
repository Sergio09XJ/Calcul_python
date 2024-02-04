#Este programa suma dos numeros: 

lista = [1,2,3,4,5,6,7,8,9,10]
lista_2 = [10,9,8,7,6,5,4,3,2,1]
suma = lambda x, y: x + y 

lista_f = list(map(lista,lista_2, suma))
print(lista_f)