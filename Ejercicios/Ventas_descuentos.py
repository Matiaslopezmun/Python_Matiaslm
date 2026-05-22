total=0
cupon_usado=False

Menu= """
------------MENU--------------
1.Comprar producto A ($10.000)
2.Comprar producto B ($20.000)
3.Aplicar cupon de descuento
4.Pagar y Salir
------------------------------
"""
while True:
    print(Menu)
    try:
        op=int(input("Seleccione una opcion: "))
        match op:
            case 1:
                total+=10000
                print("Usted ha comprado el producto A")
            case 2:
                total+=20000
                print("Usted ha comprado el producto B")
            case 3:
                desc=input("Ingrese el cupon de descuento: ")
                if desc=="DESCUENTO10" and cupon_usado==False:
                    total=int(total*0.90)
                    cupon_usado=True
                    print("Cupon aplicado correctamente")
                elif desc=="DESCUENTO10" and cupon_usado==True:
                    print("El cupon ya fue utilizado")
                else:
                    print("Cupon invalido")
            case 4:
                print(f"Su total a pagar es de ${total}, muchas gracias.")
            case _:
                print("Operacion invalida")
    except:
        print("#ERROR# Ingrese solo numeros enteros.")



