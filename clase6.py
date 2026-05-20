#PuntosAcumulados
sw = 1
puntos = 100000

while sw==1:
    try:
        print("1. Ver mis puntos")
        print("2. Gastar mis puntos")
        print("3. Salir")
        op=int(input("Seleccione una opción: "))

        match op:
            case 1:
                print(f"Sus puntos son: {puntos}")       
            case 2:
                    if puntos==0:
                        print("Puntos insuficientes")
                        print("Seleccione el producto a canjear")
                        print("1.- Gift Card de $10.000, valor de 10.000 puntos")
                        print("2.- Secadora de pelo, valor de: 25.000 puntos")
                        print("3.- Disco duro portátil, valor de: 30.000 puntos")
                        op2=int(input("Seleccione la opción: "))
                        
                    else:
                        if op2==1:
                            if puntos<10000:
                                print("Puntos insuficientes para el canje")
                            else:
                                puntos = puntos-10000
                                print(f"Canje exitoso, le quedan: ${puntos} puntos")
                        if op2==2:
                            if puntos<25000:
                                print("Puntos insuficientes para el canje")
                            else:
                                puntos = puntos-25000
                                print(f"Canje exitoso, le quedan: ${puntos} puntos")
                        if op2==3:
                            if puntos<30000:
                                print("Puntos insuficientes para el canje")
                            else:
                                puntos = puntos-30000
                                print(f"Canje exitoso, le quedan: ${puntos} puntos")
            case 3:
                print("Muchas gracias por ocupar el servicio, adios.")
                break
            case _:
                print("Ingrese una opcion valida")
    except:
        print("ERROR #Ingrese solo numeros enteros")
