import flask
from bson.json_util import dumps
import sw.dados

bp = flask.Blueprint("naves", __name__, url_prefix="/naves")

@bp.route("")
def listar_naves():
    naves = dumps(list(sw.dados.naves()))
    return flask.Response(naves, headers=sw.dados.cabecalhos)

@bp.route("", methods=["POST"])
def criar_nave():
    nave = flask.request.json
    sw.dados.naves.append(nave)
    id = len(sw.dados.naves) - 1
    return flask.jsonify({"id": id})

@bp.route("/<int:id>", methods=["PUT"])
def modificar_nave(id):
    nave = flask.request.json
    sw.dados.naves[id] = nave
    return flask.jsonify({"ok": True})

@bp.route("/<int:id>")
def get_nave(id):
    nave = dumps(list(sw.dados.naves())[id])
    return flask.Response(nave, headers=sw.dados.cabecalhos)