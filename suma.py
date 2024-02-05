#Este programa suma dos numeros: 
print("\n Este programa suma las 2 listas: \n")

lista = [1,2,3,4,5,6,7,8,9,10]
lista_2 = [10,9,8,7,6,5,4,3,2,1]
suma = lambda x, y: x + y 

#Correjimos el eror al cambiar suma y lista de orden, map primero toma la función.
lista_f = list(map(suma,lista_2, lista))
print("\n El resultado de cada suma en las listas es: ")
print(lista_f, "\n")