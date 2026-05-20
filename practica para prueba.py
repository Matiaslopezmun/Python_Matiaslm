import random as rd

balas=5
puntaje_total=0
tiros_perfectos=0

name=input("Ingrese su nombre: ")
while name=="":
    print("Error")
    name=input("Ingrese su nombre: ")


print("MENU")
print("")
print("1.Disparar")
print("2.Recargar")
print("3.Salir")

opcion=input("Seleccione una opcion: ")

match opcion:
    case "1":
        if balas>0:
            if rd==10:
                tiros_perfectos=tiros_perfectos+1
            else:
                puntaje_total=puntaje_total+rd.randint(0, 10)  
            print(f"Disparando {tiros_perfectos}, {puntaje_total}")           
        else:
            print("No hay balas")

    case "2":
        print("Recargando...")
    case "3":
        print("Haz salido correctamente.")
    case _:
        print("Opcion no elegible")


