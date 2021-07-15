import flask

app = flask.Flask(__name__)

@app.route("/")
def home():
    return 'Olá Mundo! da 4 Linux'

@app.route("/saudar/<nome>")
def saudar(nome):
    return f"Saudações {nome}!"

@app.route("/user/<int:id>")
def user(id):
    return f"Página do usuário {id}"

@app.route("/apenas-post", methods=["POST"])
def apenas_post():
    return ''

if __name__ == "__main__":
    app.run(debug=True)