pacientes=[
    {"nombre":" Aquiles Baeza", "prevension":"Fonasa","temperatura":34.6,"grave":False}
]

pacientes.append({"nombre":" Aquiles Baeza", "prevension":"Isapre","temperatura":39.6,"grave":False})

def valores():
    atencion=25000
    print(f"\nPreviciones: \n[1] Fonasa \n[2] Isapre \n[3] Fodesa")
    op=int(input("Seleccione una opcion: "))
    if op==1:
        fonasa=0.46
        Desc=atencion*fonasa
        print(f"El precio final es de {Desc}")
    elif op==2:
        isapre=0.73
        Desc=atencion*isapre
        print(f"El precio final es de {Desc}")
    elif op==3:
        fodesa=0.875
        Desc=atencion*fodesa
        print(f"El precio final es de {Desc}")
    else:
        print("Ingrese una opcion valida.")
  
def temperatura():
    temp=int(input("Ingrese la temperatura: "))
    if temp>=39:
        return True
    else:
        return False


def AgregarPacientes():
    nombre=input("Ingrese el nombre del paciente: ")
    valores()
    temperatura()

AgregarPacientes()