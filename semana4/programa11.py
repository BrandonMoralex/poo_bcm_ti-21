"""
Programa11
Nombre: Brandon CM
Fecha: 9/02/2023
Descripcion:Comparacion de dos numeros y pruevas
"""
def mayor (numero1,numero2): #funcion para sacar el mayor de los número impuestos
    result=None
    if numero1 > numero2: #mayor qur
        result=numero1 #imprime el numero 1
    elif numero2 > numero1: #mayor qur
        result=numero2 #imprime el numero2

    return result #permite regresar el valor   

print(mayor(2,3)) #imprimen el numero que es mayor 
print(mayor(2,5))#imprimen el numero que es mayor 
print(mayor(2,3.5))#imprimen el numero que es mayor 
print(mayor(2,-8))#imprimen el numero que es mayor 
print(mayor(2,6))#imprimen el numero que es mayor 
print(mayor(2,-2))#imprimen el numero que es mayor 
print(mayor(2,10))#imprimen el numero que es mayor 
print(mayor(2,9.5))#imprimen el numero que es mayor 


"""
#pythoni

def mayor (numero1:int,numero2:int)->int|None:
    result=None
    if numero1 > numero2:
        result=numero1
    elif numero2 > numero1:
        result=numero2 
        
    return result #permite regresar el valor

print(mayor(3.5,2))
print(mayor(2,-2))
print(mayor(-2,1))
print(mayor(5,2.3))
print(mayor(-12,12))
print(mayor(2,1))
print(mayor(1.5,-11))
print(mayor(12.1,-123.2))
"""