productos=[]

def MostrarProducto():
    if len(productos)==0:
        print("El inventario esta vacio")
    else:
        c=1
        for p in productos:
            print(f"{c}.- Nombre: {p['nombre']} | Precio: ${p['precio']} | Stock: {p['stock']}")
            c += 1

def AgregarProdcuto():
    nombre=input("Que producto deseas agregar?: ")
    precio=int(input("Cual es el valor?: "))
    stock=int(input("Ingresa la cantidad de productos a agregar: "))
    productos.append({"nombre":nombre, "precio":precio, "stock":stock})

def VenderProducto():
    if len(productos) == 0:
        print("No hay productos para vender.")
        return
        
    MostrarProducto()
    seleccion = int(input("¿Cuál producto desea vender? (Ingrese el número): "))

    if productos[seleccion - 1]["stock"] > 0:
        productos[seleccion - 1]["stock"] -= 1  # Le restamos 1 al stock actual
        print(f"Venta realizada. Nuevo stock: {productos[seleccion - 1]['stock']}")
    else:
        print("Lo sentimos, no queda stock de este producto.")
    
while True:
    try:
        op=int(input("\nINVENTARIO \n[1]. Agregar producto \n[2]. Vender producto \n[3]. Mostrar productos \n[4]. Salir\nSeleccione un producto: "))
        match op:
                case 1: 
                    AgregarProdcuto()
                case 2:
                    VenderProducto()
                case 3:
                    MostrarProducto()
                case 4:
                    print("Saliendo...")
                    break
                case _:
                    print("Ingrese una opcion valida")
    except:("Error")