#importacion de las funciones del programa que estan en otro codigo
#el cual esta llamado como f.py pero podria tener otro nombre
import f
#es la creacion de la biblioteca que contiene los datos de los trabajadores 
#la cual de momento esta vacia
registro = []
#el while true puede ser remplazable por un while con una variable que se tendria
#que definir previamente
while True:
    print("Menu principal")
    print("1. Registrar trabajador ")
    print("2. Listar los todos los trabajadores") 
    print("3.print(Imprimir planilla de sueldos) ")
    print("4.print(Salir del Programa)")
    #se puede usar la funcion menu o usar if y elif pero menu es mas practico
    #ya que no requiere verificaciones exautivas
    menu=input("selecciona una opcion..: ")
    if menu == "1":
        print("Registrar")
        #llamado a la funcion registrar en el programa f
        f.registrar(registro)

    elif menu == "2":
        print("Listar")
        #llamado a la funcion listar 
        f.listar(registro)
    elif menu == "3":
        print("imprimiendo...")
        #llamando a la funcion imprimir 
        f.imprimir(registro)

    elif menu == "4":
        print("saliendo...")
        #break rompe el codigo, si se uso un booleano 
        #habria que poner el booleano contrario al decreto
        break