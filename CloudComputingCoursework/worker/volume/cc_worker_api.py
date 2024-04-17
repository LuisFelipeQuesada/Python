from fastapi import FastAPI, Body
from cc_worker_github import worker_github
from cc_worker_minio import worker_minio
from pydantic import BaseModel
import os

app = FastAPI()

def crear_folder(relative_path):
    home_dir = os.path.expanduser("~")
    if "/root" in home_dir:
        new_dir = relative_path
    else:
        new_dir = home_dir + relative_path
    if not os.path.exists(new_dir):
        os.makedirs(new_dir)
    return new_dir

class Tareas(BaseModel):
    url:str

@app.post("/procesar_tarea/")
async def procesar_tarea(tareas: Tareas):
    repo_url = tareas.url
    working(repo_url)

def working(repo_url):
    relative_path = "/CC/CC/repo_descargas/"
    full_path = crear_folder(relative_path)
    full_path = full_path.replace(".git", "")
    codigo = ""
    try:
        worker_gh = worker_github(repo_url, full_path)
        worker_gh.descargar_repo()
        repo_nombre = worker_gh.obtener_repo_nombre()

        wrk_minio = worker_minio(repo_nombre, repo_nombre, full_path)
        codigo = wrk_minio.subir_archivo()
        mensaje = 'status:'+ codigo
    except Exception as e:
        mensaje = 'status:'+ codigo
        print(e)
    return {mensaje}
