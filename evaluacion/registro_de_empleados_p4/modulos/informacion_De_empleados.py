import json
import ejecutorjs.ejecutor as ee
def informacion():
    try:
        Title = """
        **************************************
        * INGRESO DE INFORMACION DE EMPLEADO *
        **************************************
        """
        print (Title)
        print ("bienvenido ingrese la informacion de su empleado")
        id = int(input("ingrese la informacion id de su empleado : "))
        nombre = input ("ingrese el nombre de su empleado con su apellido incluido : ")
        try:
            print ("1 almacenista \n2 jefe it \n3 administrador \n4 mensajero \n5 gerente")
            op = int(input("ingrese el cargo del empleado: "))
        except ValueError:
            informacion()
        match op:
            case 1:
                cargo = ("almacenista")
            case 2: 
                cargo = ("jefe it")
            case 3:
                cargo = ("administrador")
            case 4: 
                cargo = ("mensajero")
            case 5: 
                cargo = ("gerente")
        mespagado = input ("ingrese el mes en que le pagaron al empleado : ")
        fachapagado = int( input ("ingrese la fecha del pago (0/0/0) : "))
        salariobase = int(input("ingrese el salario base del empleado "))
        valordia = int(input("ingrese el valor por dia del trabajador : "))
        diastrabajados = int(input("ingrese los dias trabajados de su empleado : "))
        horasextras = int(input("ingrese las horas extras trabajadas por sus empleados : "))
        descuentocafeterio = int(input("ingrese de caunto es el descuto por pago a la cafeteria : "))
        salario = valordia*diastrabajados
        valor_horasextras = horasextras*5500
        salariotol = salario+valor_horasextras
        salariototal = salariotol-descuentocafeterio
        print (f"el salario del trabajador es de {salariototal}")
        usuario = {
            "id" : id,
            "nombre" : nombre,
            "cargo" : cargo,
            "mes pagado" : mespagado,
            "fecha pagado" : fachapagado,
            "salario base" :{
                "valor por dia" : valordia,
                "dias trabajados" : diastrabajados,
                "horas extras" : horasextras ,
                "valor horas extras" : valor_horasextras,
                "descuento cafeteria": descuentocafeterio,
                "salariototal": salariototal 
            }
        }
        ee.guardar_archivo("data",id,usuario)
        ee.informacion.get("data").update({id: usuario})
        if bool(input("desea agregar otro empleados S(si) o enter(no)")):
            informacion()
        else:
            import main
            main.menu(0)
    except ValueError:
        informacion()