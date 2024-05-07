def convertidor_Dolar():
    pesos = int(input ("ingrese la cantidad de pesos a cambiar a dolares :"))
    dolar = 3944
    conversion = pesos / dolar
    print (f"la cantidad de dolares que tienes es de {conversion} ")
    menu(0)
def convertidor_yen():
    pesos = int(input ("ingrese la cantidad de pesos a cambiar a yenes :"))
    yen = 26.30
    conversion = pesos / yen
    print (f"la cantidad de yenes que tienes es de {conversion} ")
    menu(0)
def convertidor_pesos():
    euro = int (input/"ingrese la cantidad de pesos a cambiar a euros")
    pesos = 4279
    conversion = euro*pesos
    print (f"la cantidad de pesos que tienes es de {conversion}")
def convertidor_euro():
    pesos = int(input("ingrese la cantidad de pesos a cambiar a euros :"))
    euro = 4279
    conversion = pesos / euro
    print (f"la cantidad de euros que tienes es de {conversion}")
    menu(0)
def menu(op):
    title = """
    ******************
    * MENU DE CAMBIO *
    ******************
    """
    try:
        print (title)
        print ("1.convertir a dolares \n2 convertir a yenes \n3 convertir a euroc \n4 convertir a pesos \n5 salir")
        op = int(input("ingrese a la occion a utilizar : ")) 
    except ValueError:
        menu(0)
    match op:
        case 1:
            convertidor_Dolar()
        case 2:
            convertidor_yen()
        case 3:
            convertidor_euro()
        case 4: 
            convertidor_pesos()
        case 5: 
            print ("gracias por utilizar")
        case _:
            print ("error vuelva a intentarlo")
            menu(0)
menu(0)