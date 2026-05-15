from flask import Blueprint, request, jsonify

from modelos.paper import Paper
from repositorios.repositorio_paper import RepositorioPaper

paper_bp = Blueprint("paper", __name__, url_prefix="/paper")
repositorio = RepositorioPaper()


@paper_bp.get("/")
def obtener_todos():
    papers = repositorio.obtener_todos()
    return jsonify([paper.get_diccionario() for paper in papers])


@paper_bp.post("/")
def crear():
    datos = request.get_json()

    if not datos or not datos.get("doi") or not datos.get("titulo") or not datos.get("id_autor"):
        return jsonify({"Mensaje": "Verificar los datos de entrada para registrar"}), 400

    paper = Paper(
        titulo=datos["titulo"],
        doi=datos["doi"],
        id_autor=datos["id_autor"]
    )

    repositorio.crear(paper)

    return jsonify(paper.get_diccionario()), 201


@paper_bp.put("/<int:id>")
def actualizar(id):
    datos = request.get_json()

    if not datos or not datos.get("doi") or not datos.get("titulo") or not datos.get("id_autor"):
        return jsonify({"Mensaje": "Verificar los datos de entrada para actualizar"}), 400

    paper = repositorio.obtener_por_id(id)

    if not paper:
        return jsonify({"Mensaje": "Paper no encontrado"}), 404

    paper.titulo = datos["titulo"]
    paper.doi = datos["doi"]
    paper.id_autor = datos["id_autor"]

    repositorio.actualizar(paper)

    return jsonify(paper.get_diccionario()), 200


@paper_bp.delete("/<int:id>")
def eliminar(id):
    paper = repositorio.obtener_por_id(id)

    if not paper:
        return jsonify({"Mensaje": "Paper no encontrado"}), 404

    repositorio.eliminar(id)

    return jsonify({"Mensaje": "Paper eliminado correctamente"}), 200