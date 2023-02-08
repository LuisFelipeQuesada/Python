import git
import re

class worker_github:

    __repo_url = ""
    __repo_nombre = ""
    __ruta_descarga = ""

    def __init__(self, repo_url, ruta_descarga):
        # Obtener url del repo
        self.__repo_url = repo_url
        self.__repo_usuario, self.__repo_nombre = repo_url.split("/")[-2:]
        self.__ruta_descarga = ruta_descarga
    
    def descargar_repo(self):
        try:
            self.__repo_url = re.sub(r'"', '', self.__repo_url)
            #
            self.__repo_nombre = re.sub(r'"', '', self.__repo_nombre)
            self.__repo_nombre = re.sub(r'\'', '', self.__repo_nombre)
            #
            git.Repo.clone_from(self.__repo_url, self.__ruta_descarga + self.__repo_nombre)
        except Exception as e:
            print(e)
    
    def obtener_repo_nombre(self):
        return self.__repo_nombre
