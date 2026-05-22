numero_secreto=42
intentos=5

while intentos>0:
    try:
        print(f"\nTe quedan {intentos} intentos.")
        adivina=int(input("Adivina el numero: "))
        if adivina==numero_secreto:
            print("GANASTE")
            break
        elif adivina<numero_secreto:
            print("El numero secreto es mayor")
            intentos-=1
        elif adivina>numero_secreto:
            print("El numero secreto es menor")
            intentos-=1
        if intentos==0:
            print("Perdiste, el numero era 42")

    except ValueError:
        print("Solo puedes ingresar numeros enteros (No pierdas intentos)")