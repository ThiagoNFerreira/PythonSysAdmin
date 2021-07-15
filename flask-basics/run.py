import flask
import sw.naves.blueprint as naves
from config.db import setup

app = flask.Flask(__name__)  # dois underlines
app.register_blueprint(naves.bp)

@app.route("/")
def home():
    return 'home'

@app.route("/personagens")
def listar_personagens():
    return flask.jsonify(sw.personagens)

if __name__ == "__main__":  # também com 2 underlines
    setup()
    app.run(debug=True)
