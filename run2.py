import flask
import sw.naves
import sw.personagens
import sw.veiculos
import sw.dados

app = flask.Flask(__name__)
app.register_blueprint(sw.naves.bp)
app.register_blueprint(sw.personagens.bp)
app.register_blueprint(sw.veiculos.bp)

if __name__ == "__main__":
    sw.dados.setup()
    app.run(debug=True)