"""
Programa4
Nombre: Brandon CM
Fecha: 26/01/2023
Descripcion: Comentarios multilinea, Comentarios de una linea, Concatenacion de cadenas y cadena de caracteres
"""
numero1= 10
numero2= 5
print("{} + {} = {}".format(numero1,numero2,numero1 + numero2)) #este esta bien

print("{n1} + {n2} = {suma}".format(n1=numero1,n2=numero2,suma=numero1 + numero2)) #sirve porque declaramos el valor

print("{n2} + {n2} = {n2}".format(n1=numero1,n2=numero2,suma=numero1 + numero2)) #si sirve pero se debe agregar el valor de n2 5+5=5

print("{n4} + {n4} = {n4}".format(n1=numero1,n2=numero2,suma=numero1 + numero2))

print("{numero1} + {numero2} = {suma}".format(numero1=numero1, numero2=numero2, suma=numero1 + numero2)) 
print("{numero1} + {numero2} = {}".format(numero1,numero2,numero1 + numero2)) #no sirve porque no declaramos el valor

