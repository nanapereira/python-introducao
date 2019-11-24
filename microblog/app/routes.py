from app import app
from flask import render_template

@app.route('/')
@app.route("/index")
def index():
    user = {'username': 'Nana'}
    posts = [
        {
            'author': {'username': 'Jhon'},
            'body': 'Beautiful day in Florianópolis!'
        },
        {
            'author': {'username': 'Nana'},
            'body': 'The Star Wars movie was so cool!'
        }
    ]
    soma = {'resultado': 1989 - 1986}
    return render_template('index.html', title='Pagina inicial', user=user, posts=posts, soma=soma)