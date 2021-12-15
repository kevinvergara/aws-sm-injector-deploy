# !/bin/env python
import os, json

def inicio():
    try:
        #extraer nombre de secreto
        path_secrets = os.environ["PATH_SECRETS_JSON"]
        path_container_config = os.environ["PATH_CONTAINER_JSON"]

        #extraer secretos
        with open(path_secrets, 'rt') as file_json:
            secretos = json.load(file_json)

        #extraer container config
        with open(path_container_config, 'rt') as file_json:
            containers_config = json.load(file_json)
        
        #recorrer json y armar string para archivo de secretos
        export_json = []
        for key in secretos:
            value = secretos[key]
            export_json.append({"value": value.encode('utf-8'), "name": key.encode('utf-8')})
        
        containers_config["environment"] = export_json

        print(json.dumps(containers_config))

        #crear archivo
        crear_archivo(json.dumps(containers_config))
    except:
        print("error en inicio")
        
def crear_archivo(export_string):
    try:
        #extraer nombre de archivo y ruta
        nombre_archivo = "container_config_secrets.json"

        #crear archivo y guardar informacion
        file_env = open(nombre_archivo, "w")
        file_env.write(export_string)
        file_env.close()
    except:
            print("error en crear_archivo")
#inicio del script
inicio()