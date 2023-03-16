"""
Programa7
Nombre: Brandon CM
Fecha: 31/01/2023
Descripcion: Comentarios multilinea, Comentarios de una linea, Concatenacion de cadenas y cadena de caracteres y acalcular areas y perimetros.
"""
print ("Area y perimetro de un circulo") #imprime el area la cual se saca asi El área de un círculo es pi multiplicado por el radio al cuadrado (A = π r²). 
diametro= float(input("ingrese el diametro de tu circulo:")) #Meta el dato del diametro
radio= diametro/2 #formula de diametro
area= (3.1416)*(radio)*(radio) #formula de área 
perimetro = (2)*(3.1416)*(radio) #formula de perímetro 
print("El área del circulo de {} su radio es {}".format(diametro,area))# Ingrese el area, despues del paso anterior
print("El perímetro de un circulo {} su radio es {}".format(diametro,perimetro))#ingrese el dato del perimetro


print("") #Este dato me lo dieron mis amigos y es para dar un espacio

print ("Area y perimetro de un cuadrado")#imprime lo que haremos
lado= float(input("ingrese los lados del cuadrado:")) #da la orden para hacerlo
area= lado*lado #formula de area
perimetro= lado+lado+lado+lado #formula de perímetro 
print("El area de un cuadrado es {}".format(lado*lado))#da el resultado del dato que pusiste
print("el perimetro de un cuadrado es {}".format(lado+lado+lado+lado))#da el dato del perimetro