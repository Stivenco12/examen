print ("bienvenido ingrese la informacion de su empleado")
id = input("ingrese la informacion id de su empleado : ")
nombre = input ("ingrese el nombre de su empleado con su apellido incluido : ")    
apellidos = input("ingrese el apellido: ")
ubicasion = input ("ingrese la ubicasion : ")
direccion = input ("ingrese la direccion : ")
ciudad = input ("ingrese el nombre de la ciudad : ")
logintud = input ("ingrese la longitud : ")
latitud = input ("ingrese la latitud : ")
email = input ("ingrese su correao : ")
edad = int(input ("ingrese su edad : "))
ocupacion = input("ingrese el trabajo principal : ")

usuario = {
    "id" : id,
    "nombre" : nombre,
    "apellidos" : apellidos,
    "ubicasion" : {
        "direccion": direccion,
        "ciudad" : ciudad,
        "logintud" : logintud,
        "latitud" : latitud,
    },
    "email" : email,
    "edad" : edad,
    "ocupacion" : ocupacion
}
print (usuario)