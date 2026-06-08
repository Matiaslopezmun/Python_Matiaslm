# print(list(vegetales.items())[-1])
# print(list(vegetales.keys())[-1])

vegetales={1:"Maracuya",2:"Pera",3:"Cebolla",4:"Papa"}

def agregarVegetal():
    print("-"*40)
    agregar=input("ingrese un vegetal: ")
    nuevokey=list(vegetales.keys())[-1]
    vegetales[nuevokey+1]=agregar

def mostrarVegetales():
    print("-"*40)
    for num, nombre in vegetales.items():
        print(f"{num}.- {nombre} ")

def eliminarVegetal():
    mostrarVegetales()
    eliminar=int(input("Seleccione un vegetal a eliminar: "))
    del vegetales[eliminar]
    print("Nombre del vegetal eliminado correctamente")

def actualizarVegetal():
    mostrarVegetales()
    actualizar=int(input("Seleccione el vegetal que desea actualizar: "))
    vegetales[actualizar]=input("Ingrese el nuevo nombre: ")
    print("Nombre del vegetal actualizado correctamente")
 
def vegetalesMenu():
    while True:
        try:
            print("-"*40)
            print("1. Agragar vegetal")
            print("2. Eliminar vegetal")
            print("3. Actualizar vegetal")
            print("4. Mostrar vegetal")
            print("5. Salir")
            op=int(input("Seleccione una opcion: "))
            match op:
                case 1:
                    agregarVegetal()
                case 2:
                    eliminarVegetal()
                case 3:
                    actualizarVegetal()
                case 4:
                    mostrarVegetales()
                case 5:
                    print("Saliendo del programa...")
                    break
                case _:
                    print("Opcion invalida")
        except:
            print("Ingrese caracteres validos.")

# vegetalesMenu()

##Diccionario con diccionarios
productosDiscc={
    1:{"nombre": "maracuya", "precio": 3000},
    2:{"nombre": "pera", "precio": 1500},
    3:{"nombre": "cebolla", "precio": 1200}
}

productosDiscc[4]={"nombre": "piña", "precio": 3500}

for num, veg in productosDiscc.items():
    print(f"{num}.- {veg}")

def agregarProdcuto():
    nombre=input("Ingrese el nombre del producto: ")
    precio=int(input("Ingrese el precio del producto: "))
    nuevokey=list(productosDiscc.keys())[-1]
    productosDiscc[nuevokey+1]={"nombre": nombre, "precio": precio}

def eliminarProducto():
    mostrarProductos()
    eliminar=int(input("Seleccion el producto a eliminar: "))
    del productosDiscc[eliminar]

def actualizarProdcutos():
    mostrarProductos()
    actualizar=int(input("Que producto desea actualizar: "))
    nombre=input("Cual es el nombre nuevo: ")
    precio=int(input("Cuales el precio nuevo: "))
    productosDiscc[num]={"nombre": nombre, "precio": precio}

def mostrarProductos():
    for key, prodcutos in productosDiscc.items():
        print(f"{key}, {prodcutos}")

def vegetalesMenuDiccionario():
    while True:
        try:
            print("-"*40)
            print("1. Agragar vegetal")
            print("2. Eliminar vegetal")
            print("3. Actualizar vegetal")
            print("4. Mostrar vegetal")
            print("5. Salir")
            op=int(input("Seleccione una opcion: "))
            match op:
                case 1:
                    agregarProdcuto()
                case 2:
                    eliminarProducto()
                case 3:
                    actualizarVegetal()
                case 4:
                    mostrarProductos()
                case 5:
                    print("Saliendo del programa...")
                    break
                case _:
                    print("Opcion invalida")
        except:
            print("Ingrese caracteres validos.")

vegetalesMenuDiccionario()