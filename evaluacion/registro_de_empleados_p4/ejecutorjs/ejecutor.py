import json
import os 

MY_DATA_BASE = "data/inicio.json"

def ingresar_informacion_json(*param):
    datos = list(param)
    with open(MY_DATA_BASE,"r+") as rwf:
        archivos_data=json.load(rwf)
        if (len(param) > 1):
            archivos_data[datos[0]].update({datos[1]:datos[2]})
        else:
            archivos_data.update({param[0]})
        rwf.seek(0)
        json.dump(archivos_data,rwf,indent=4)
def leer_archivo():
    with open(MY_DATA_BASE,"r") as rf:
        return json.load(rf)
def guardar_archivo(*param):
    data = list(param)
    if(os.path.isfile(MY_DATA_BASE)):
        if(len(param)):
            data[0].update(leer_archivo())
informacion= {
    "data" : {}
}