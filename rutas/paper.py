from flask import Blueprint, request, jsonify

from modelos.paper import Paper

from repositorios.repositorio_paper import RepositorioPaper

paper_bp = Blueprint("paper", __name__, url_prefix="/paper")
repositorio = RepositorioPaper()

@paper_bp.get("/")
def obtener_todos():
    papers = repositorio.obtener_todos()
    return jsonify([paper.get_diccionario() for paper in papers])