import os
import secrets
from datetime import timedelta

from flask import (
    Flask, render_template, request,
    redirect, url_for, session
)
from werkzeug.security import check_password_hash

app = Flask(__name__)

secret_key = os.environ.get("SECRET_KEY")
usuario_valido = os.environ.get("LOGIN_USER")
senha_hash = os.environ.get("LOGIN_PASSWORD_HASH")

if not all([secret_key, usuario_valido, senha_hash]):
    raise RuntimeError(
        "Configure SECRET_KEY, LOGIN_USER "
        "e LOGIN_PASSWORD_HASH."
    )

app.secret_key = secret_key
app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(
    minutes=30
)
app.config["SESSION_COOKIE_HTTPONLY"] = True
app.config["SESSION_COOKIE_SAMESITE"] = "Lax"
app.config["SESSION_COOKIE_SECURE"] = (
    os.environ.get("COOKIE_SECURE") == "1"
)

@app.route("/")
def inicio():
    return redirect(url_for("login"))

@app.route("/login", methods=["GET", "POST"])
def login():

    if session.get("usuario"):
        return redirect(url_for("boas_vindas"))

    erro = None
    if request.method == "POST":
        usuario = request.form.get("usuario", "")
        senha = request.form.get("senha", "")

        usuario_correto = secrets.compare_digest(
            usuario.encode("utf-8"),
            usuario_valido.encode("utf-8")
        )
        senha_correta = check_password_hash(
            senha_hash, senha
        )

        if usuario_correto and senha_correta:
            session.clear()
            session.permanent = True
            session["usuario"] = usuario_valido
            session["csrf_token"] = secrets.token_urlsafe(32)
            return redirect(url_for("boas_vindas"))

        erro = "Usuario ou senha incorretos."

    return render_template("login.html", erro=erro)

@app.route("/boas-vindas")
def boas_vindas():
    if not session.get("usuario"):
        return redirect(url_for("login"))

    return render_template(
        "boas_vindas.html",
        usuario=session["usuario"],
        csrf_token=session["csrf_token"]
    )


@app.route("/sair", methods=["POST"])
def sair():
    token = request.form.get("csrf_token", "")
    if not session.get("usuario"):
        return redirect(url_for("login"))

    if not secrets.compare_digest(
        token, session.get("csrf_token", "")
    ):
        return "Requisicao invalida.", 400

    session.clear()
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=False)
