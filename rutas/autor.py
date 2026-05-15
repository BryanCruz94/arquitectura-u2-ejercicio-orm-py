from flask import Blueprint, request, jsonify

from modelos.autor import Autor

from repositorios.repositorio_autor import RepositorioAutor

autor_bp = Blueprint("autor", __name__, url_prefix="/autor")
repositorio = RepositorioAutor()

@autor_bp.get("/")
def obtener_todos():
    autores = repositorio.obtener_todos()
    return jsonify([autor.get_diccionario() for autor in autores])
