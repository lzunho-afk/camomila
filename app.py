from flask import Flask
from flask import render_template
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Home</h1>"

@app.post('/login')
def login_post():
    return "<b>LOGGED?</b>"

@app.get('/login')
def login_get():
    return render_template('login.html')

@app.route('/user/<username>')
def show_user_profile(username):
    return f'Profile do usuário {escape(username)}'

@app.route('/network/<path:netpath>')
def show_network(netpath):
    return f'Caminho para a rede de serviço {escape(netpath)}'
