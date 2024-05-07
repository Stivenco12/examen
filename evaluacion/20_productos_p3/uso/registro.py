import ejecutors.eje as ee
def registroproduc():
    id = input ("ingrese la id del producto : ")
    nombre = input ("ingrese el nombre del producto : ")
    valorunitario = int(input ("ingrese el valor del producto : "))
    stockmin = int (input ("ingrese el stock minimo del producto : "))
    stockmax = int (input ("ingrese el stock maximo del producto : "))
    producto = {
        "id" : id,
        "nombre" : nombre,
        "valorunitario" : valorunitario,
        "stockmin" : stockmin,
        "stockmax" : stockmax
    }
    ee.ingresar_informacion_json("data",id)
    ee.informacion.get("data").update({id})
    if bool(input("desea agregar otro empleados S(si) o enter(no)")):
        registroproduc()
    else:
        import main
        main.menu