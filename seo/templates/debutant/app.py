from flask import Flask, render_template

app = Flask(__name__)
app.config["SECRET_KEY"] = "votre-cle-secrete-changez-moi"

@app.route("/")
def accueil():
    return render_template("index.html", titre="Bienvenue")

@app.route("/a-propos")
def a_propos():
    return render_template("a_propos.html", titre="À propos")

if __name__ == "__main__":
    print(" Application Flask démarrée sur http://localhost:5000")
    app.run(debug=True)
