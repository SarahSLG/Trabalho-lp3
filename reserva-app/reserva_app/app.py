from flask import Flask, render_template

app = Flask("reservas")

@app.route("/")
def login():
    return render_template('login.html')

@app.route("/cadastro")
def cadastrar_pessoa():
    return render_template('cadastro.html')


@app.route("/cadastrar_sala")
def cadastrar_sala():
    return render_template('cadastrar-sala.html')

@app.route("/reservar-sala")
def reservar_sala():
    return render_template('reservar-sala.html')

@app.route("/listar_salas")
def listar_sala():
    return render_template('listar-salas.html')

@app.route("/reservas")
def reservas():
    return render_template('reservas.html')