import ejecutors.eje as ee
import uso.registro as ur
def menu(op):
    try:
        if op != 5:
            title = """
            ************************
            * MENU DE 20 PRODUCTOS *
            ************************
            """
            try:
                print (title)
                print ("1 ingresar la informacion del productos \n2 historial \n3 salir")
                op = int(input("ingrese unas de las occiones a elejir: "))
            except ValueError:
                pass
            match op:
                case 1:
                    ur.registroproduc()
                case 2:
                    pass
                case 3:
                    print ("saliendooooo..................")
                case _:
                    menu(0)
    except ValueError:
        menu(0)
if __name__ == "__main__":
    ee.MY_DATA = "data/inicio.json"
    ee.guardar_archivo(ee.informacion)
    menu(0)