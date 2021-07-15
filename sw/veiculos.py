import flask
import sw.dados

bp = flask.Blueprint("veiculos", __name__, url_prefix="/veiculos")

@bp.route("")
def listar_veiculo():
    return flask.jsonify(sw.dados.veiculo)

@bp.route("", methods=["POST"])
def criar_veiculo():
    veiculo = flask.request.json
    sw.dados.veiculo.append(veiculo)
    id = len(sw.dados.veiculo) - 1
    return flask.jsonify({"id": id})

@bp.route("/<int:id>", methods=["PUT"])
def modificar_veiculo(id):
    veiculo = flask.request.json
    sw.dados.veiculo[id] = veiculo
    return flask.jsonify({"ok": True})