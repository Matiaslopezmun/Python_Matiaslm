## Uso y explicacion de random

import random
import time

# num=random.randint(1,10)

# for i in range(num):
#     print("Hola")

# strike=random.randint(10, 70)

# if strike>50:
#     print("Its a critrical hit, Damage:", strike)

# else:
#     print("Its not very effective. Damage:", strike)


## 3 personas juegan golf 
## cada persona tiene la prosibilidad de golpear 
## y la distancia varia entre 60 y 190 
## mostrar al final el golpe mas fuerte



# j1=random.randint(60, 190)
# j2=random.randint(60, 190)
# j3=random.randint(60, 190)

# print(f"El jugador 1 golpeo la pelota a: {j1} metros")
# print(f"El jugador 2 golpeo la pelota a: {j2} metros")
# print(f"El jugador 3 golpeo la pelota a: {j3} metros")


# if j1>j2 and j1>j3:
#     print("El jugador uno hizo el tiro mas lejano")
# elif j2>j3:
#     print("El jugador dos hizo el tiro mas lejano")
# else:
#     print("El jugador tres hizo el tiro mas lejano")


## KILLER INSTINC

# Dos peleadores se piden al iniico de la pelea
# Cada peleador inicia con 100 de HP
# se debe hace una pelea por turnos
# y cada golpe varia entre 7 y 18
# se termina el match cuando uno de los 2 tiene su hp menor o igual a 0
# se debe mostrar al ganador al final
# bonus: mostrar las barras de energia de cada peleador


# hp1=100
# hp2=100


# peleador1=input("Ingrese el peleador 1: ")
# peleador2=input("Ingrese el peleador 2: ")


# golpe=random.randint(7, 18)
# print("Turno del peleador 1")
# print("Daño realizado", golpe)
# print("Vida Total del enemigo:", hp2-golpe)

# golpe=random.randint(7, 18)
# print("Turno del peleador 2")
# print("Daño realizado", golpe)
# print("Vida Total del enemigo:", hp1-golpe)

# p1=input("Ingrese el nombre del personaje: ")
# p2=input("Ingrese el nombre del personaje: ")

# hp1=100
# hp2=100
# turno=random.randint(1,2)

# while hp1>0 and hp2>0:

#     if turno%2==0:
#         print(f"Turno de {p1}")
#         atk=random.randint(7,18)
#         print(f"El {p1} ataca con {atk}")
#         hp2-=atk
#         print(f"La vida restante del jugador {p2} es de: {hp2}")
#         time.sleep(3)

#     else:
#         print(f"Turno de {p2}")
#         atk=random.randint(7,18)
#         print(f"El {p2} ataca con {atk}")
#         hp1-=atk
#         print(f"La vida restante del jugador {p1} es de: {hp1}")
#         time.sleep(3)
#     turno==+1

# if hp2>hp2:
#     print(f"El jugador {p1} a ganado")
    
# else:
#     print(f"El jugador {p2} a ganado")


