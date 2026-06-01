juguetes=["yo-yo", "tetris"]
menu= """
-----------------------------------
-        MENU DE JUGUETES         -
-----------------------------------
1.Agregar juguete
2.ELiminar juguete
3.Actualizar juguete
4.Mostrar Juguetes
5.Salir
-----------------------------------
"""
def mostrarJuguetes():
    for j in range(len(juguetes)):
        print(f"{j+1}.- {juguetes[j]}")
def mostrarJ():
    print("-"*20)
    c=1
    for i in juguetes:
        print(f"{c}.- {i}")
        c+=1

while True:
    try:
        print(menu)
        op=int(input("Seleccione una opcion: "))
        print("-"*35)
        match op:
            case 1:
                agregar=input("ingrese un juguete: ")
                juguetes.append(agregar)
            case 2:
                mostrarJuguetes()
                eliminar=int(input("Seleccione un juguete a eliminar: "))
                juguetes.pop(eliminar-1)
                print(f"Usted a eliminado con exito el juguete {juguetes[eliminar-1]}")
            case 3:
                mostrarJuguetes()
                actualizar=int(input("Seleccione el juguete que desea actualizar: "))
                juguetes[actualizar-1]=input("Ingrese el nuevo nombre: ")
                print("Nombre de juguete actualizado exitosamente.")
            case 4:
                mostrarJuguetes()
            case 5:
                print("Saliendo del programa...")
                break
            case _:
                print("Opcion invalida")
    except:
        print("Ingrese caracteres validos.")