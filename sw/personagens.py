import flask
import sw.dados

bp = flask.Blueprint("personagens", __name__, url_prefix="/personagens")

@bp.route("")
def listar_personagens():
    return flask.jsonify(sw.dados.personagens)

# @bp.route("/<int:id>", methods=["PUT"])
# def modificar_personagen(id):
#     personagens = flask.request.json
#     sw.personagens[id] = personagens
#     return flask.jsonify({"ok": True})

# # @bp.route("")
# # def listar_personagens():
# #     return flask.jsonify(sw.personagens)

# @bp.route("<int:id>")
# def get_personagens(id):
#     return flask.jsonify(sw.personagens[id])