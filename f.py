

def registrar(registro):
    #aqui se preguntan los datos para guardarlos en la biblioteca
    nombre = input("nombre del trabajador: ")
    apellido = input("apellido del trabajador: ")
    cargo = input("cargo del trabajador: ")
    sueldo_bruto = int(input("ingresar sueldo bruto del trabajador :"))
    desc_salud= 70000
    desc_afp=120000
    sueldo_liquido=(sueldo_bruto - desc_salud - desc_afp)

    #aqui se guardan los datos previamente requridos 
    datos= { 
        #la estructura siempre es: "variable a guardar": "valor"(puede ser variable y no usar las comillas)
        #como se ve en este ejemplo    
        "nombre" : nombre,
        "apellido": apellido,
        "cargo": cargo,
        "sueldo_bruto":sueldo_bruto,
        "desc_salud":desc_salud,
        "desc_afp":desc_afp,
        "sueldo_liquido":sueldo_liquido
        }   
    #aqui se agregan los datos almacenados a la biblioteca antes creados 
    return registro.append(datos)

def listar (registro):
    #aqui se leen los datos guardados en la biblioteca y muestra los datos
    for trabajador in registro:
            print(f"nombre: {trabajador['nombre']} {trabajador['apellido'] }")
            print(f"cargo: {trabajador['cargo']}")
            print(f"sueldo liquido: {trabajador['sueldo_liquido']}")
            print()

def imprimir(registro):

    while True:
        print("opciones para imprimir lista")
        print("1. imprimir todas la lista")
        print("2. imprimir por cargo")
        print("3. volver")
        opc_lista=input()
        
        if opc_lista == "1":
             planilla(registro)
        
        elif opc_lista == "2":
            #definicion de los cargos
            cargos=["CEO","Programador","Analista de datos","Diseñador"]
            print(cargos)
            cargo_buscar=input("que cargo estas buscando: ")
            #aqui pone un condicional para verificar si el cargo es el que se busca
            if cargo_buscar in cargos:
                with open("planilla.txt", "w") as planilla_trabajador:
                    for trabajador in registro:
                        if trabajador['cargo'] == cargo_buscar:
                            planilla_trabajador.write(f"nombre: {trabajador['nombre']} {trabajador['apellido']}\n")
                            planilla_trabajador.write(f"cargo: {trabajador['cargo']}\n")
                            planilla_trabajador.write(f"sueldo liquido: {trabajador['sueldo_liquido']}\n")
                            planilla_trabajador.write("\n")
                        

        elif opc_lista == "3":
            print("volviendo...")
            print()
            break

def planilla(registro):
    
    with open("planilla.txt", "w") as planilla_trabajador:
        for trabajador in registro:
            #se escribe por lineas      la estrucuta es esta "nombre":"variable en base" y asi con todos los valores
            planilla_trabajador.write(f"nombre: {trabajador['nombre']} {trabajador['apellido'] }\n")
            planilla_trabajador.write(f"cargo: {trabajador['cargo']}\n")
            planilla_trabajador.write(f"sueldo liquido: {trabajador['sueldo_liquido']}\n")
            planilla_trabajador.write("\n")


   