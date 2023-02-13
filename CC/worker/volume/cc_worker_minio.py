import os
import re
from minio import Minio
import json
import docker
import shutil

class worker_minio:

    __ruta_credenciales = 'credenciales_minio.json'
    __servidor = ""
    __puerto = ""
    __clave_acceso = ""
    __clave_secreta = ""
    __nombre_bucket = ""
    __repo_nombre = ""
    __ruta_local_fichero = ""

    def __init__(self, nombre_bucket, repo_nombre, ruta_local_fichero):
        self.__servidor =  self.obtener_IP("cc_minio") + ":" + str(9000)#"cc_minio:9000"
        print("MINio server: " + self.__servidor)
        self.__clave_acceso = self.obtener_credenciales()[1]
        self.__clave_secreta = self.obtener_credenciales()[2]
        self.__nombre_bucket = self.limpiar_nombre_bucket(nombre_bucket.strip())
        self.__repo_nombre = repo_nombre.strip()
        self.__ruta_local_fichero = ruta_local_fichero.strip()
    
    def obtener_credenciales(self):
        try:
            ruta = os.path.dirname(os.path.abspath(__file__)) + "/" + self.__ruta_credenciales
            file = open(ruta, 'r')
            data = json.loads(file.read())
            file.close()
            return [data['url'], data['accessKey'], data['secretKey']]
        except Exception as e:
            return e
    
    def limpiar_nombre_bucket(self, nombre_bucket):
        try:
            nombre_bucket = re.sub(r'"', '', nombre_bucket)
            nombre_bucket = nombre_bucket.lower()
            return nombre_bucket
        except Exception as e:
            print(e)
    
    def obtener_IP(self, name):
        client = docker.from_env()
        contenedores = client.containers.get(name)
        ip = contenedores.attrs["NetworkSettings"]["Networks"]["cc_backend"]["IPAddress"]
        return ip
    
    def subir_archivo(self):
        try:
            # Obtener cliente
            cliente = Minio(endpoint=self.__servidor, access_key=self.__clave_acceso, secret_key=self.__clave_secreta, secure=False)
            print(self.__ruta_local_fichero)

            # Crear bucket si no existe.
            found = cliente.bucket_exists(self.__nombre_bucket)
            if not found:
                cliente.make_bucket(self.__nombre_bucket)

            # Subir el archivo al bucket correspondiente
            for raiz, dirs, archivos in os.walk(self.__ruta_local_fichero):
                for archivo in archivos:
                    cliente.fput_object(self.__nombre_bucket, os.path.join(raiz, archivo).replace(self.__ruta_local_fichero, ""), os.path.join(raiz, archivo))
            os.chdir(self.__ruta_local_fichero)
            print("Borrar directorio" + self.__repo_nombre)
            shutil.rmtree(self.__repo_nombre)
            return "200"
        except Exception as e:
            print(e)
            return "400"
