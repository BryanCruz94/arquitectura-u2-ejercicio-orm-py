from flask import Blueprint, request, jsonify

from modelos.autor import Autor
from repositorios.repositorio_autor import RepositorioAutor

autor_bp = Blueprint("autor", __name__, url_prefix="/autor")
repositorio = RepositorioAutor()


@autor_bp.get("/")
def obtener_todos():
    autores = repositorio.obtener_todos()
    return jsonify([autor.get_diccionario() for autor in autores])


@autor_bp.post("/")
def crear():
    datos = request.get_json()

    if not datos or not datos.get("nombre") or not datos.get("pais"):
        return jsonify({"Mensaje": "Verificar los datos de entrada para registrar"}), 400

    autor = Autor(
        nombre=datos["nombre"],
        pais=datos["pais"]
    )

    repositorio.crear(autor)

    return jsonify(autor.get_diccionario()), 201


@autor_bp.put("/<int:id>")
def actualizar(id):
    datos = request.get_json()

    if not datos or not datos.get("nombre") or not datos.get("pais"):
        return jsonify({"Mensaje": "Verificar los datos de entrada para actualizar"}), 400

    autor = repositorio.obtener_por_id(id)

    if not autor:
        return jsonify({"Mensaje": "Autor no encontrado"}), 404

    autor.nombre = datos["nombre"]
    autor.pais = datos["pais"]

    repositorio.actualizar(autor)

    return jsonify(autor.get_diccionario()), 200


@autor_bp.delete("/<int:id>")
def eliminar(id):
    autor = repositorio.obtener_por_id(id)

    if not autor:
        return jsonify({"Mensaje": "Autor no encontrado"}), 404

    repositorio.eliminar(id)

    return jsonify({"Mensaje": "Autor eliminado correctamente"}), 200