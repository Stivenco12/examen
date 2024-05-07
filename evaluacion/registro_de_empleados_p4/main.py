import modulos.informacion_De_empleados as ide
import ejecutorjs.ejecutor as ee
def menu(op):
    try:
        if op != 5:
            title = """
            *****************
            * MENU DE PAGOS *
            *****************
            """
            try:
                print (title)
                print ("1 ingresar informacion de empleado \n2 salir")
                op = int(input("ingrese unas de las occiones a elejir: "))
            except ValueError:
                pass
            match op:
                case 1:
                    ide.informacion()
                case 2:
                    print ("saliendoo..................")
                case _:
                    menu(0)
    except ValueError:
        menu(0)
if __name__ == "__main__":
    ee.MY_DATA_BASE = "data/inicio.json"
    ee.guardar_archivo(ee.informacion)
    menu(0)