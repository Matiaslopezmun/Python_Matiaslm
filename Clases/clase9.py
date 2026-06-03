# #Sin argumento y sin retorno
# def saludo():
#     print("hola que tal?")

# #Sin argumento y con retorno
# def suma():
#     num1=3
#     num2=5
#     return(num1+num2)
# print(suma())

# def esMayor():
#     edad=24
#     if edad>18:
#         return True
#     else:
#         return False
# resultado=suma()
# print(esMayor())

# # Con argumento y sin retorno
# def saludame(name):
#     print("Hola", name)

# saludame("Matias")

# def calculaIVA(neto):
#     print(f"El precio con IVA es {neto*1.19}")

# calculaIVA(4000)

# # Con argumento y retorno
# def sumaCA(n1,n2):
#     return(n1+n2)

# def calcularIVAca(neto):
#     return neto*1.19

# print("El resultado es:",sumaCA(7,10))
# print("El total con iva es:", calcularIVAca(10000))

# v=int(input("Ingrese el valor neto: "))
# print("El total con iva es:", v*1.19)

##CALCULADORA CON FUNCIONES##

# n1=int(input("Ingrese el primr numero: "))
# n2=int(input("Ingrese el segundo numero: "))

# while True:
#     print("Que operacion desea realizar:\n1.Sumar \n2.Restar \n3.Multiplicar \n4.Dividir \n5.Salir ")
#     op=int(input("Seleccione una opion: "))

#     def suma(n1, n2):
#         return n1+n2
#     def resta(n1, n2):
#         return n1-n2
#     def multiplicar(n1, n2):
#         return n1*n2
#     def dividir(n1, n2):
#         if n2==0:
#             return "No se puede dividir por 0"
#         else:
#             return n1/n2

#     match op:
#         case 1: 
#             print(suma(n1,n2))
#         case 2:
#             print(resta(n1,n2))
#         case 3:
#             print(multiplicar(n1,n2))
#         case 4:
#             print(dividir(n1,n2))
#         case 5:
#             print("Saliendo del sistema")
#             break
#         case _:
#             print("ingrese una opcion correcta")


cnotas=int(input("Ingrese la cantidad de notas: "))
notas=[]
for n in range(cnotas):
    nota=int(input(f"Ingrese su nota {n+1}: "))
    notas.append(nota)

def calcularProm(notas):
    return int(sum(notas)/len(notas))

print("EL promedio es", calcularProm(notas), notas)


        
    

